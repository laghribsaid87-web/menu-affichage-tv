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

# The perfect split background: Wood texture at the bottom 40%, solid dark gray wall on top.
perfect_bg = "url('https://images.unsplash.com/photo-1546484396-fb3fc6f95f98?ixlib=rb-4.0.3&w=1920&q=80') bottom/100% 40% no-repeat, linear-gradient(to bottom, #111111 0%, #1e1e1e 100%)"

components = []

# Flying leaves (chjirat) to make it dynamic
components.append({"type": "customText", "content": "🌿", "x": -500, "y": -150, "scale": 3, "color": "#ffffff", "fontSize": 50, "fontFamily": "Inter", "hasShadow": True, "strokeColor": "#000000", "z": 15, "animIn": "fadeDown", "animOut": "zoomOut", "delay": 0.4})
components.append({"type": "customText", "content": "🍃", "x": 400, "y": 0, "scale": 2.5, "rotation": 45, "color": "#ffffff", "fontSize": 50, "fontFamily": "Inter", "hasShadow": True, "strokeColor": "#000000", "z": 15, "animIn": "fadeDown", "animOut": "zoomOut", "delay": 0.7})
components.append({"type": "customText", "content": "🌿", "x": 550, "y": -200, "scale": 2, "rotation": -30, "color": "#ffffff", "fontSize": 50, "fontFamily": "Inter", "hasShadow": True, "strokeColor": "#000000", "z": 15, "animIn": "fadeRight", "animOut": "zoomOut", "delay": 0.9})

# The Main Sandwich (Perfectly sitting on the wooden table)
components.append({
    "type": "main", "assetId": "sandwiche americain.png", 
    "x": -150, "y": 150, "scale": 2.2, 
    "rotation": 0, "z": 10, 
    "animIn": "fadeUp", "animOut": "fadeDown", "delay": 0, "continuousAnim": "pulse"
})

# Fries slightly behind
components.append({
    "type": "main", "assetId": "frite.png", 
    "x": 350, "y": 100, "scale": 1.5, 
    "rotation": 10, "z": 9, 
    "animIn": "fadeUp", "animOut": "fadeDown", "delay": 0.2
})

# Drink slightly behind
components.append({
    "type": "main", "assetId": "coca.png", 
    "x": 600, "y": 80, "scale": 1.4, 
    "rotation": 0, "z": 8, 
    "animIn": "fadeLeft", "animOut": "fadeLeft", "delay": 0.3
})

data = {
    "assets": base_assets,
    "orientation": "horizontal",
    "formules": {
        "formule_main": {
            "name": "MENU ROYAL",
            "description": "L'expérience Ultime",
            "price": "55 DH",
            "badge": "NOUVEAU",
            "duration": 20,
            "bgEffect": "steam", # Dak Skhonya (Steam)
            "bgColor": perfect_bg, # M9sem 3la 2
            
            # Title on the wall (Top left)
            "nameLayout": {"x": -450, "y": -350, "scale": 2, "rotation": 0, "animIn": "fadeDown", "delay": 0, "z": 20},
            "descLayout": {"x": -450, "y": -250, "scale": 1.5, "rotation": 0, "animIn": "fadeRight", "delay": 0.2, "z": 20},
            
            # Price Badge (Large Circle like Vloo)
            "priceLayout": {"x": -500, "y": -50, "scale": 3.5, "rotation": -10, "animIn": "zoomIn", "delay": 0.5, "z": 20},
            
            # Badge
            "badgeLayout": {"x": 0, "y": -350, "scale": 1.5, "rotation": 15, "animIn": "fadeDown", "delay": 0.4, "z": 30},
            
            "components": components,
            "tv": "1",
            "isGeneratingIA": False
        }
    }
}

with open(os.path.join(menu_dir, "menu_data_vloo_1.json"), 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
