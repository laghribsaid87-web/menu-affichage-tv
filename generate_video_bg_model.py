import json
import os

menu_dir = r"c:\Users\pc\Desktop\menu"

base_assets = {
    "drinks": [{"id": "coca.png", "name": "coca", "url": "processed_images/coca.png"}],
    "sandwiches": [
        {"id": "bocadillo cheese.png", "name": "bocadillo cheese", "url": "processed_images/bocadillo cheese.png"},
        {"id": "sandwiche americain.png", "name": "sandwiche americain", "url": "processed_images/sandwiche americain.png"}
    ],
    "sides": [{"id": "frite.png", "name": "frite", "url": "processed_images/frite.png"}]
}

components = []
components.append({
    "type": "main", "assetId": "sandwiche americain.png", 
    "x": 0, "y": 150, "scale": 2, 
    "rotation": 0, "z": 10, 
    "animIn": "fadeUp", "animOut": "fadeDown", "delay": 0, "continuousAnim": "pulse"
})

data = {
    "assets": base_assets,
    "orientation": "horizontal",
    "formules": {
        "formule_main": {
            "name": "MENU VIDEO",
            "description": "Background Animé",
            "price": "40 DH",
            "badge": "VIDEO",
            "duration": 20,
            "bgEffect": "none",
            "bgColor": "processed_images/test_video.mp4", # VIDEO HERE
            "nameLayout": {"x": 0, "y": -350, "scale": 1.5, "rotation": 0, "animIn": "fadeDown", "delay": 0, "z": 20},
            "descLayout": {"x": 0, "y": -250, "scale": 1.2, "rotation": 0, "animIn": "fadeRight", "delay": 0.2, "z": 20},
            "priceLayout": {"x": 400, "y": 0, "scale": 2, "rotation": 0, "animIn": "zoomIn", "delay": 0.5, "z": 20},
            "badgeLayout": {"x": -400, "y": -200, "scale": 1.5, "rotation": -15, "animIn": "fadeLeft", "delay": 0.4, "z": 30},
            "components": components,
            "tv": "1",
            "isGeneratingIA": False
        }
    }
}

with open(os.path.join(menu_dir, "menu_data_video_1.json"), 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
