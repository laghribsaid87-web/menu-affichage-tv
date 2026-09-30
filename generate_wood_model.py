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

def create_model(filename, bg_effect, bg_color, components, name, price, badge=""):
    data = {
        "assets": base_assets,
        "orientation": "horizontal",
        "formules": {
            "formule_main": {
                "name": name,
                "description": "L'expérience authentique",
                "price": price,
                "badge": badge,
                "duration": 25,
                "bgEffect": bg_effect,
                "bgColor": bg_color,
                "nameLayout": {"x": 0, "y": -420, "scale": 1.5, "rotation": 0, "animIn": "fadeDown", "delay": 0, "z": 20},
                "descLayout": {"x": 0, "y": -350, "scale": 1, "rotation": 0, "animIn": "fadeUp", "delay": 0.2, "z": 20},
                "priceLayout": {"x": 0, "y": 450, "scale": 2, "rotation": 0, "animIn": "zoomIn", "delay": 0.5, "z": 20},
                "badgeLayout": {"x": -600, "y": -420, "scale": 1.2, "rotation": -15, "animIn": "fadeLeft", "delay": 0.4, "z": 30},
                "components": components,
                "tv": "1",
                "isGeneratingIA": False
            }
        }
    }
    with open(os.path.join(menu_dir, filename), 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

comp_wood = []

# Wooden background URL (dark wood texture)
wood_bg = "url('https://images.unsplash.com/photo-1546484396-fb3fc6f95f98?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80') center/cover no-repeat"

# 4 large items distributed across the entire screen
positions = [
    {"x": -600, "y": 0, "asset": "bocadillo cheese.png", "price": "35 DH", "delay": 0.2},
    {"x": -200, "y": -50, "asset": "sandwiche americain.png", "price": "45 DH", "delay": 0.4},
    {"x": 200, "y": 50, "asset": "bocadillo cheese.png", "price": "40 DH", "delay": 0.6},
    {"x": 600, "y": -20, "asset": "frite.png", "price": "15 DH", "delay": 0.8}
]

for p in positions:
    # The image
    comp_wood.append({
        "type": "main", "assetId": p["asset"], "x": p["x"], "y": p["y"], "scale": 1.2, 
        "rotation": 0, "z": 10, "animIn": "zoomIn", "animOut": "zoomOut", "delay": p["delay"], "exitTime": 24, "continuousAnim": "glow"
    })
    
    # A dark circle behind price for readability on wood
    comp_wood.append({
         "type": "shape",
         "shapeType": "badge",
         "x": p["x"] + 100, "y": p["y"] + 120,
         "width": 120, "height": 120,
         "color": "#aa0000", "color2": "#660000", "isGradient": True,
         "z": 14, "opacity": 1,
         "animIn": "fadeUp", "delay": p["delay"] + 0.1, "borderRadius": 60
    })
    
    # The price text
    comp_wood.append({
        "type": "customText",
        "content": p["price"],
        "x": p["x"] + 100,
        "y": p["y"] + 120,
        "scale": 1,
        "color": "#ffffff",
        "fontSize": 32,
        "fontFamily": "Inter",
        "hasShadow": True,
        "strokeColor": "#000000",
        "z": 15,
        "animIn": "fadeUp",
        "animOut": "fadeDown",
        "delay": p["delay"] + 0.2
    })

# Add smoke effect to make the wooden background feel like a hot grill
create_model("menu_data_model11_1.json", "smoke", wood_bg, comp_wood, "MENU RUSTIQUE", "DEPUIS 1999", "TOP")
