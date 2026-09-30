import os
import json
import uuid
import subprocess
from flask import Flask, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

app = Flask(__name__)

# Config
MENU_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(MENU_DIR, 'menu_data.json')
RAW_IMAGES_DIR = os.path.join(MENU_DIR, 'raw_images')
PROCESSED_IMAGES_DIR = os.path.join(MENU_DIR, 'processed_images')

# Ensure directories exist
os.makedirs(RAW_IMAGES_DIR, exist_ok=True)
os.makedirs(PROCESSED_IMAGES_DIR, exist_ok=True)

@app.route('/')
def index():
    return send_from_directory(MENU_DIR, 'dashboard.html')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory(MENU_DIR, filename)

@app.route('/api/projects', methods=['GET'])
def get_projects():
    projects = {'default': 4}
    for f in os.listdir(MENU_DIR):
        if f.startswith('menu_data_') and f.endswith('.json'):
            # format: menu_data_{project}_{tv_id}.json
            parts = f.replace('menu_data_', '').replace('.json', '').split('_')
            if len(parts) >= 2:
                proj_name = parts[0]
                try:
                    tv_id = int(parts[1])
                except:
                    tv_id = 1
                if proj_name not in projects or tv_id > projects[proj_name]:
                    projects[proj_name] = tv_id
    return jsonify(projects)

@app.route('/api/menu/<project>/<tv_id>', methods=['GET'])
def get_project_menu(project, tv_id):
    file_path = os.path.join(MENU_DIR, f'menu_data_{project}_{tv_id}.json')
    if not os.path.exists(file_path) and project == 'default' and tv_id == '1':
        file_path = DATA_FILE
        
    try:
        if not os.path.exists(file_path):
            return jsonify({})
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/menu/<project>/<tv_id>', methods=['POST'])
def save_project_menu(project, tv_id):
    file_path = os.path.join(MENU_DIR, f'menu_data_{project}_{tv_id}.json')
    try:
        data = request.json
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/projects/<project>', methods=['DELETE'])
def delete_project(project):
    if project == 'default':
        return jsonify({"error": "Cannot delete default project"}), 400
    try:
        deleted = False
        for f in os.listdir(MENU_DIR):
            if f.startswith(f'menu_data_{project}_') and f.endswith('.json'):
                os.remove(os.path.join(MENU_DIR, f))
                deleted = True
        if deleted:
            return jsonify({"success": True})
        return jsonify({"error": "Project not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/designer', methods=['POST'])
def ai_designer():
    if not GROQ_API_KEY or GROQ_API_KEY == 'your_groq_api_key_here':
        return jsonify({"error": "Veuillez configurer votre clé API Groq dans le fichier .env"}), 401
    
    try:
        client = Groq(api_key=GROQ_API_KEY)
        req_data = request.json
        prompt = req_data.get('prompt', '')
        assets_context = json.dumps(req_data.get('assets', {}))
        
        system_prompt = f"""
You are an expert graphic designer and UI engineer. The user wants to build a digital signage menu layout on a 1920x1080 canvas.
The canvas coordinate system centers at X=0, Y=0. Max limits are approximately X: -800 to 800, Y: -400 to 400.
You have the following assets available:
{assets_context}

Based on the user's prompt, create a JSON structure for a formula. 
The JSON must have this exact structure (NO MARKDOWN, ONLY PURE JSON):
{{
    "name": "Catchy Name (Do not copy user prompt)",
    "description": "Short appetizing description",
    "price": 50,
    "badge": "Promo Text",
    "duration": 6,
    "bgColor": "radial-gradient(circle at 50% 60%, #1a1a1a 0%, #000000 100%)",
    "components": [
        {{
            "assetId": "...",
            "type": "main|side|drink",
            "x": 0,
            "y": 0,
            "scale": 1,
            "rotation": 0,
            "z": 5,
            "animIn": "fadeLeft|fadeRight|fadeUp|fadeDown|zoomIn",
            "animOut": "fadeLeft|fadeRight|fadeUp|fadeDown|zoomOut",
            "delay": 0.2
        }},
        {{
            "type": "customText",
            "content": "MENU NAME HERE",
            "x": 0,
            "y": -300,
            "scale": 1,
            "color": "#ffffff",
            "fontSize": 90,
            "fontFamily": "Impact",
            "hasShadow": true,
            "strokeColor": "#000000",
            "z": 10,
            "animIn": "zoomIn",
            "animOut": "zoomOut",
            "delay": 0.5
        }}
    ]
}}
IMPORTANT: 
- bgColor should be a valid CSS property. Examples: 'linear-gradient(to bottom, #87CEEB, #fecfef)' for a beach/sky vibe, etc. If the user mentions a color/theme, use a cool gradient.
- Position elements logically. E.g. 2 sandwiches? put them side by side (X=-250, X=250). Drink? put it in the back (Z=2) at Y=-150.
- ALWAYS include at least one 'customText' component to show the Name of the menu, and position it at Y=-300!
- You cannot generate external images. If user asks for 'a beach', just use a beach-like CSS gradient and use the closest food assets you have!
"""
        completion = client.chat.completions.create(
            model="qwen/qwen3.8-27b",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=1500
        )
        
        response_text = completion.choices[0].message.content.strip()
        # Clean up any potential markdown formatting from the response
        if response_text.startswith("```json"):
            response_text = response_text[7:]
        if response_text.endswith("```"):
            response_text = response_text[:-3]
            
        json_resp = json.loads(response_text.strip())
        return jsonify({"success": True, "formula": json_resp})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/designer_edit', methods=['POST'])
def ai_designer_edit():
    if not GROQ_API_KEY or GROQ_API_KEY == 'your_groq_api_key_here':
        return jsonify({"error": "Veuillez configurer votre clé API Groq dans le fichier .env"}), 401
    
    try:
        client = Groq(api_key=GROQ_API_KEY)
        req_data = request.json
        prompt = req_data.get('prompt', '')
        current_formula = json.dumps(req_data.get('formula', {}))
        assets_context = json.dumps(req_data.get('assets', {}))
        
        system_prompt = f"""
You are an expert graphic designer and UI engineer for a digital signage CMS. 
The user wants to MODIFY an existing screen/formula based on their prompt.
The canvas is 1920x1080, coordinate system centers at X=0, Y=0.

Available assets:
{assets_context}

Current Formula JSON:
{current_formula}

INSTRUCTIONS:
1. Understand what the user wants to change (e.g., 'animate the burger', 'add a shape', 'change background to red', 'add a price').
2. Modify the Current Formula JSON accordingly. If they ask to add a product/asset, append it to the components list with appropriate position.
3. If they ask to animate, update `animIn`, `animOut`, or `continuousAnim` properties of the relevant component.
4. If they ask for a background, update `bgColor` (CSS gradient/color).
5. RETURN ONLY THE FULLY MODIFIED FORMULA JSON. NO MARKDOWN, NO EXPLANATIONS. PURE JSON ONLY.
"""
        completion = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=2000
        )
        
        response_text = completion.choices[0].message.content.strip()
        if response_text.startswith("```json"):
            response_text = response_text[7:]
        if response_text.endswith("```"):
            response_text = response_text[:-3]
            
        json_resp = json.loads(response_text.strip())
        return jsonify({"success": True, "formula": json_resp})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/vision_designer', methods=['POST'])
def ai_vision_designer():
    if not GROQ_API_KEY or GROQ_API_KEY == 'your_groq_api_key_here':
        return jsonify({"error": "Veuillez configurer votre clé API Groq dans le fichier .env"}), 401
    
    try:
        client = Groq(api_key=GROQ_API_KEY)
        req_data = request.json
        base64_image = req_data.get('image', '')
        assets_context = json.dumps(req_data.get('assets', {}))
        
        system_prompt = f"""
You are an expert graphic designer and UI engineer. The user wants to CLONE the layout of the provided reference image for a digital signage menu on a 1920x1080 canvas.
The canvas coordinate system centers at X=0, Y=0. Max limits are approximately X: -800 to 800, Y: -400 to 400.

You have the following assets available in your system:
{assets_context}

Analyze the provided image and create a JSON structure for a formula that mimics its layout.
CRITICAL LAYOUT RULES:
1. DO NOT OVERLAP TEXT. Spread elements across the X and Y axes logically! 
2. If the original image has columns (e.g. Base, Viande, Sauce), space them out on the X axis (e.g. X: -500, -150, 200, 550).
3. Group lists of items into a SINGLE `customText` component using `\\n` for new lines, instead of creating 20 separate text components.
4. Align titles at the top (Y: -350 to -250) and content below them.
5. Set `fontSize` appropriately (Titles: 60-90, Normal text: 20-40).
6. If the image has a specific background color, set `bgColor` to a matching CSS color or gradient.
7. Use ONLY the available image assets. If the image shows a tacos but you only have a bocadillo, use the bocadillo asset and position it where the tacos was.

The JSON must have this exact structure (NO MARKDOWN, ONLY PURE JSON):
{{
    "name": "Catchy Name Based on Image",
    "description": "Short appetizing description",
    "price": 50,
    "badge": "Promo Text",
    "duration": 6,
    "bgColor": "radial-gradient(circle at 50% 60%, #1a1a1a 0%, #000000 100%)",
    "components": [
        {{
            "assetId": "...",
            "type": "main|side|drink",
            "x": 0,
            "y": 0,
            "scale": 1,
            "rotation": 0,
            "z": 5,
            "animIn": "zoomIn",
            "animOut": "zoomOut",
            "delay": 0.2
        }},
        {{
            "type": "customText",
            "content": "COLUMN 1 TITLE\\nItem 1\\nItem 2",
            "x": -400,
            "y": 0,
            "scale": 1,
            "color": "#ffffff",
            "fontSize": 40,
            "fontFamily": "Impact",
            "hasShadow": true,
            "strokeColor": "#000000",
            "z": 10
        }}
    ]
}}
IMPORTANT: 
- RETURN ONLY THE FULLY VALID JSON. NO MARKDOWN, NO EXPLANATIONS. PURE JSON ONLY.
"""
        gemini_api_key = os.getenv('GEMINI_API_KEY')
        if not gemini_api_key:
            return jsonify({"error": "Veuillez configurer GEMINI_API_KEY dans votre fichier .env pour utiliser l'IA de vision."}), 401

        base64_data = base64_image.split(",")[1] if "," in base64_image else base64_image
        mime_type = "image/jpeg"
        if "png" in base64_image.split(",")[0]:
            mime_type = "image/png"

        import requests
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent?key={gemini_api_key}"
        payload = {
            "contents": [{
                "parts": [
                    {"text": system_prompt + "\n\nRecreate this layout as a JSON formula."},
                    {"inline_data": {"mime_type": mime_type, "data": base64_data}}
                ]
            }],
            "generationConfig": {
                "temperature": 0.2,
                "responseMimeType": "application/json"
            }
        }
        res = requests.post(url, json=payload)
        if not res.ok:
            raise Exception(f"Gemini API Error: {res.text}")
            
        response_text = res.json()["candidates"][0]["content"]["parts"][0]["text"]
        if response_text.startswith("```json"):
            response_text = response_text[7:]
        if response_text.endswith("```"):
            response_text = response_text[:-3]
            
        json_resp = json.loads(response_text.strip())
        return jsonify({"success": True, "formula": json_resp})
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


@app.route('/api/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    target = request.form.get('target', 'raw') # 'raw' or 'root'
    
    if file:
        original_filename = secure_filename(file.filename)
        # Avoid naming collisions by prepending a short uuid
        filename = f"{uuid.uuid4().hex[:8]}_{original_filename}"
        if target == 'root':
            save_path = os.path.join(MENU_DIR, filename)
            url_path = filename
        else:
            save_path = os.path.join(RAW_IMAGES_DIR, filename)
            url_path = f"raw_images/{filename}"
            
        file.save(save_path)
        return jsonify({"success": True, "path": url_path, "filename": filename})

@app.route('/api/process_images', methods=['POST'])
def process_images():
    try:
        # Run the existing process_images.py script
        script_path = os.path.join(MENU_DIR, 'process_images.py')
        result = subprocess.run(['python', script_path], capture_output=True, text=True)
        if result.returncode == 0:
            return jsonify({"success": True, "output": result.stdout})
        else:
            return jsonify({"success": False, "error": result.stderr}), 500
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/inpaint', methods=['POST'])
def inpaint_image():
    try:
        import cv2
        import numpy as np
        import base64
        import time
        
        data = request.json
        image_b64 = data.get('image', '').split(',')[1] if ',' in data.get('image', '') else data.get('image', '')
        mask_b64 = data.get('mask', '').split(',')[1] if ',' in data.get('mask', '') else data.get('mask', '')
        
        # Decode image
        img_data = base64.b64decode(image_b64)
        nparr = np.frombuffer(img_data, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        # Decode mask
        mask_data = base64.b64decode(mask_b64)
        mask_nparr = np.frombuffer(mask_data, np.uint8)
        mask = cv2.imdecode(mask_nparr, cv2.IMREAD_GRAYSCALE)
        
        # Resize mask to match image if needed
        if img.shape[:2] != mask.shape[:2]:
            mask = cv2.resize(mask, (img.shape[1], img.shape[0]))
            
        # Inpaint
        result = cv2.inpaint(img, mask, 5, cv2.INPAINT_TELEA)
        
        # Save result
        filename = f"inpainted_{int(time.time())}.png"
        filepath = os.path.join(PROCESSED_IMAGES_DIR, filename)
        cv2.imwrite(filepath, result)
        
        resp = {"success": True, "path": f"processed_images/{filename}"}
        print("INPAINT SUCCESS RESP:", resp)
        return jsonify(resp)
    except Exception as e:
        print(f"Inpaint Error: {e}")
        return jsonify({"success": False, "error": str(e)})

if __name__ == '__main__':
    print("Démarrage du Serveur CMS Digital Signage...")
    app.run(host='0.0.0.0', port=8000, debug=True)
