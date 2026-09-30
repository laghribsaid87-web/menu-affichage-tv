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
                "nameLayout": {"x": -450, "y": -400, "scale": 1.5, "rotation": -5, "animIn": "fadeLeft", "delay": 0, "z": 20},
                "descLayout": {"x": 0, "y": -330, "scale": 1.2, "rotation": 0, "animIn": "fadeUp", "delay": 0.2, "z": 20},
                "priceLayout": {"x": 0, "y": -400, "scale": 2.5, "rotation": 0, "animIn": "zoomIn", "delay": 0.5, "z": 20},
                "badgeLayout": {"x": -600, "y": -450, "scale": 1.2, "rotation": -15, "animIn": "fadeLeft", "delay": 0.4, "z": 30},
                "components": components,
                "tv": "1",
                "isGeneratingIA": False
            }
        }
    }
    with open(os.path.join(menu_dir, filename), 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def generate_bottom_row(num_items, y_img, y_text, scale):
    comps = []
    assets_pool = ["bocadillo cheese.png", "sandwiche americain.png"]
    total_width = 1600
    start_x = -(total_width // 2)
    gap = total_width // (num_items - 1) if num_items > 1 else 0
    
    # Add a dark background bar for the bottom row to separate it
    comps.append({
         "type": "shape",
         "shapeType": "badge",
         "x": 0, "y": 300,
         "width": 1920, "height": 350,
         "color": "#111111", "color2": "#222222", "isGradient": True,
         "z": 1, "opacity": 0.8,
         "animIn": "fadeUp", "delay": 0
    })

    for i in range(num_items):
        asset = assets_pool[i % len(assets_pool)]
        x = start_x + (i * gap)
        delay = i * 0.1
        
        comps.append({
            "type": "main", "assetId": asset, "x": x, "y": y_img, "scale": scale, 
            "rotation": 0, "z": 10, "animIn": "fadeUp", "animOut": "fadeDown", "delay": delay, "exitTime": 19
        })
        
        comps.append({
            "type": "customText",
            "content": f"MENU {i+1}\\n25 DH",
            "x": x,
            "y": y_text,
            "scale": 1,
            "color": "#ffffff",
            "fontSize": int(24),
            "fontFamily": "Inter",
            "hasShadow": False,
            "strokeColor": "#000000",
            "z": 15,
            "animIn": "fadeUp",
            "animOut": "fadeDown",
            "delay": delay + 0.1
        })
    return comps

# Model 9: Video Style (Fire Theme)
comp_m9 = []
comp_m9.extend([
    {"type": "main", "assetId": "sandwiche americain.png", "x": 350, "y": -100, "scale": 1.6, "rotation": -5, "z": 10, "animIn": "fadeRight", "animOut": "zoomOut", "delay": 0, "continuousAnim": "pulse"},
    {"type": "main", "assetId": "frite.png", "x": -50, "y": -50, "scale": 1.2, "rotation": 5, "z": 9, "animIn": "fadeUp", "animOut": "zoomOut", "delay": 0.2},
    {"type": "main", "assetId": "coca.png", "x": -300, "y": -80, "scale": 1.2, "rotation": -10, "z": 8, "animIn": "fadeLeft", "animOut": "zoomOut", "delay": 0.4}
])
comp_m9.extend(generate_bottom_row(6, y_img=250, y_text=380, scale=0.5))

create_model("menu_data_model9_1.json", "fire", "radial-gradient(circle at 50% 30%, #5a0000 0%, #000000 100%)", comp_m9, "DOUBLE CHEESE", "45 DHS", "NEW")

# Model 10: Video Style (City/Neon Theme)
comp_m10 = []
comp_m10.extend([
    {"type": "main", "assetId": "bocadillo cheese.png", "x": 400, "y": -120, "scale": 1.5, "rotation": 0, "z": 10, "animIn": "zoomIn", "animOut": "fadeRight", "delay": 0, "continuousAnim": "glow"},
    {"type": "main", "assetId": "frite.png", "x": 0, "y": -60, "scale": 1.3, "rotation": -5, "z": 9, "animIn": "fadeUp", "animOut": "fadeDown", "delay": 0.2},
    {"type": "main", "assetId": "coca.png", "x": -350, "y": -80, "scale": 1.3, "rotation": 5, "z": 8, "animIn": "fadeLeft", "animOut": "fadeLeft", "delay": 0.4}
])
comp_m10.extend(generate_bottom_row(6, y_img=250, y_text=380, scale=0.5))

create_model("menu_data_model10_1.json", "neon", "linear-gradient(to bottom, #000022 0%, #000000 100%)", comp_m10, "ROYAL BACON", "55 DHS", "PROMO")
