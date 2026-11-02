import os
import json
import shutil
import re

desktop = r"C:\Users\pc\Desktop"
images_dir = os.path.join(desktop, "MENU_FINAL_TV_MJABED")
menu_dir = os.path.join(desktop, "menu")
processed_dir = os.path.join(menu_dir, "processed_images")

# Ensure processed images dir exists
os.makedirs(processed_dir, exist_ok=True)

# List all images
images = [f for f in os.listdir(images_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

formules = {}
assets = {"sandwiches": [], "drinks": [], "sides": []}

# Assign to TVs (we have 3 TVs)
# TV 1: items 0, 1, 2, 3
# TV 2: items 4, 5, 6, 7
# TV 3: items 8, 9, 10
tvs = ["1", "2", "3"]

for idx, img in enumerate(images):
    name_part = os.path.splitext(img)[0]
    
    price = ""
    match = re.search(r'(\d+)\s*(dh|dhs|)', name_part, re.IGNORECASE)
    if match:
        price = match.group(1)
        name = name_part[:match.start()].strip()
    else:
        name = name_part
        price = "0"
        
    name = name.upper().replace("_", " ")
    
    # Copy image
    src = os.path.join(images_dir, img)
    dst = os.path.join(processed_dir, img)
    shutil.copy2(src, dst)
    
    asset_url = f"processed_images/{img}"
    
    # Distribute over 3 TVs evenly
    if idx < 4:
        tv_id = "1"
    elif idx < 8:
        tv_id = "2"
    else:
        tv_id = "3"
        
    f_id = f"formule_{idx}"
    
    assets["sandwiches"].append({
        "id": img,
        "name": name,
        "url": asset_url
    })
    
    formules[f_id] = {
        "id": f_id,
        "name": name,
        "description": "NOUVEAU & DÉLICIEUX",
        "price": price,
        "badge": "SPÉCIALITÉS",
        "duration": 8,
        "bgColor": "#000000",
        "bgEffect": "none",
        "tv": tv_id,
        "nameLayout": {"x": 0, "y": -400, "scale": 1.2, "rotation": 0, "animIn": "fadeDown", "delay": 0.2, "z": 20},
        "descLayout": {"x": 0, "y": -330, "scale": 0.7, "rotation": 0, "animIn": "fadeRight", "delay": 0.4, "z": 20},
        "priceLayout": {"x": -700, "y": 250, "scale": 1.8, "rotation": -15, "animIn": "rollIn", "delay": 0.6, "z": 30},
        "badgeLayout": {"x": 700, "y": -350, "scale": 1.1, "rotation": 15, "animIn": "pop", "delay": 0.5, "z": 30},
        "components": [
            {
                "type": "rawImage",
                "url": asset_url,
                "x": 0, "y": 0, "scale": 1, "z": 5,
                "continuousAnim": "pulse",
                "animIn": "zoomIn",
                "delay": 0,
                "fillScreen": True
            },
            {
                "type": "customText", "content": "✨", "x": -450, "y": 150, "scale": 2.5, "z": 25,
                "animIn": "fadeUp", "delay": 0.8, "continuousAnim": "float"
            },
            {
                "type": "customText", "content": "🔥", "x": 450, "y": 100, "scale": 3, "z": 25,
                "animIn": "fadeDown", "delay": 0.9, "continuousAnim": "breathe"
            }
        ]
    }

menu_data = {
    "orientation": "horizontal",
    "assets": assets,
    "formules": formules,
    "promos": {
        "video": "",
        "image": "",
        "videoDuration": 0,
        "imageDuration": 0
    }
}

with open(os.path.join(menu_dir, 'menu_data.json'), 'w', encoding='utf-8') as f:
    json.dump(menu_data, f, indent=2, ensure_ascii=False)

print(f"Generated {len(formules)} items across 3 TVs.")
