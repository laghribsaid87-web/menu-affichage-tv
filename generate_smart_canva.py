import json
import os
import uuid

def generate_canva_data():
    with open('config_dynamic.json', 'r', encoding='utf-8') as f:
        dynamic_data = json.load(f)

    target_file = 'menu_data_smart_1.json'
    if os.path.exists(target_file):
        with open(target_file, 'r', encoding='utf-8') as f:
            menu_data = json.load(f)
    else:
        menu_data = {"formules": {}}

    all_items = dynamic_data.get("bocadillos", []) + dynamic_data.get("sandwiches", [])

    # Clear existing formules if we are regenerating
    menu_data["formules"] = {}

    for i, item in enumerate(all_items):
        f_key = f"formule_smart_{i}_{uuid.uuid4().hex[:6]}"
        
        formule = {
            "name": f"{item['name']}",
            "tv": "1",
            "duration": 6,
            "components": []
        }

        # Shape background
        formule["components"].append({
            "type": "shape",
            "shapeType": "rect",
            "width": 1200,
            "height": 400,
            "color": "#a11111",
            "opacity": 1,
            "borderRadius": 40,
            "x": -50,
            "y": 250,
            "scale": 1,
            "z": 2,
            "animIn": "fadeIn",
            "animOut": "fadeOut",
            "delay": 0,
            "rotation": 0
        })

        # Title text
        formule["components"].append({
            "type": "customText",
            "content": item["name"],
            "x": 40,
            "y": 280,
            "scale": 1,
            "z": 15,
            "animIn": "zoomIn",
            "animOut": "zoomOut",
            "delay": 0.2,
            "rotation": 0,
            "color": "#ffffff",
            "fontSize": 70,
            "fontFamily": "'Oswald', sans-serif"
        })

        # Price text
        formule["components"].append({
            "type": "customText",
            "content": f"{item['price']} DH",
            "x": 60,
            "y": 420,
            "scale": 1,
            "z": 15,
            "animIn": "zoomIn",
            "animOut": "zoomOut",
            "delay": 0.4,
            "rotation": 0,
            "color": "#facc15",
            "fontSize": 120,
            "fontFamily": "'Oswald', sans-serif",
            "hasShadow": True
        })

        # Sandwich image
        formule["components"].append({
            "type": "image",
            "src": item["img"],
            "x": 350,
            "y": 100,
            "scale": 1.2,
            "z": 20,
            "animIn": "zoomIn",
            "animOut": "fadeOut",
            "delay": 0.6,
            "rotation": -5,
            "width": 600,
            "height": 600
        })

        # Cornet (Frites)
        formule["components"].append({
            "type": "image",
            "src": "processed_images/cornet1.png",
            "x": 650,
            "y": -20,
            "scale": 0.6,
            "z": 18,
            "animIn": "fadeIn",
            "animOut": "fadeOut",
            "delay": 0.8,
            "rotation": 0,
            "width": 400,
            "height": 400
        })

        menu_data.setdefault("formules", {})[f_key] = formule

    with open(target_file, 'w', encoding='utf-8') as f:
        json.dump(menu_data, f, indent=2, ensure_ascii=False)
    print("Generated in", target_file)

if __name__ == '__main__':
    generate_canva_data()
