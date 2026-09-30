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
                "description": "",
                "price": price,
                "badge": badge,
                "duration": 20,
                "bgEffect": bg_effect,
                "bgColor": bg_color,
                # Title perfectly centered at the top
                "nameLayout": {"x": 0, "y": -430, "scale": 1.2, "rotation": 0, "animIn": "fadeDown", "delay": 0, "z": 20},
                "descLayout": {"x": 0, "y": -330, "scale": 1, "rotation": 0, "animIn": "fadeUp", "delay": 0.2, "z": 20},
                # Price positioned to the right of the title
                "priceLayout": {"x": 500, "y": -430, "scale": 1.5, "rotation": 0, "animIn": "zoomIn", "delay": 0.5, "z": 20},
                # Badge positioned to the left
                "badgeLayout": {"x": -500, "y": -430, "scale": 1.2, "rotation": 0, "animIn": "fadeLeft", "delay": 0.4, "z": 30},
                "components": components,
                "tv": "1",
                "isGeneratingIA": False
            }
        }
    }
    with open(os.path.join(menu_dir, filename), 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def generate_bottom_row():
    comps = []
    assets_pool = ["bocadillo cheese.png", "sandwiche americain.png"]
    
    # Dark banner background for the bottom row
    comps.append({
         "type": "shape",
         "shapeType": "badge",
         "x": 0, "y": 350,
         "width": 1920, "height": 300,
         "color": "#111111", "color2": "#000000", "isGradient": True,
         "z": 1, "opacity": 0.9,
         "animIn": "fadeUp", "delay": 0
    })

    # Exact coordinates for 6 items evenly spaced across X axis
    # X values: -750, -450, -150, 150, 450, 750
    x_positions = [-750, -450, -150, 150, 450, 750]
    y_img = 280
    y_text = 420
    scale_img = 0.35  # Small enough to not overlap

    for i in range(6):
        asset = assets_pool[i % len(assets_pool)]
        x = x_positions[i]
        delay = i * 0.1
        
        comps.append({
            "type": "main", "assetId": asset, "x": x, "y": y_img, "scale": scale_img, 
            "rotation": 0, "z": 10, "animIn": "fadeUp", "animOut": "fadeDown", "delay": delay, "exitTime": 19
        })
        
        comps.append({
            "type": "customText",
            "content": f"MENU {i+1}\\n25 DH",
            "x": x,
            "y": y_text,
            "scale": 1,
            "color": "#ffffff",
            "fontSize": 26,
            "fontFamily": "Inter",
            "hasShadow": False,
            "strokeColor": "#000000",
            "z": 15,
            "animIn": "fadeUp",
            "animOut": "fadeDown",
            "delay": delay + 0.1
        })
    return comps

# Model 9: Clean Video Style (Fire Theme)
comp_m9 = []
# Hero section perfectly spaced
# Drink on left (-400), Burger in center (0), Fries on right (400)
comp_m9.extend([
    {"type": "main", "assetId": "coca.png", "x": -400, "y": -150, "scale": 1, "rotation": 0, "z": 8, "animIn": "fadeLeft", "animOut": "zoomOut", "delay": 0.4},
    {"type": "main", "assetId": "sandwiche americain.png", "x": 0, "y": -150, "scale": 1.4, "rotation": 0, "z": 10, "animIn": "zoomIn", "animOut": "zoomOut", "delay": 0, "continuousAnim": "pulse"},
    {"type": "main", "assetId": "frite.png", "x": 400, "y": -150, "scale": 1, "rotation": 0, "z": 9, "animIn": "fadeRight", "animOut": "zoomOut", "delay": 0.2}
])
# Bottom row
comp_m9.extend(generate_bottom_row())

create_model("menu_data_model9_1.json", "fire", "radial-gradient(circle at 50% 30%, #5a0000 0%, #000000 100%)", comp_m9, "DOUBLE CHEESE", "45 DHS", "NEW")
