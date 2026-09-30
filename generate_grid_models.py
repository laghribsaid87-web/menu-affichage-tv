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

def create_model(filename, bg_effect, bg_color, components, name, badge=""):
    data = {
        "assets": base_assets,
        "orientation": "horizontal",
        "formules": {
            "formule_main": {
                "name": name,
                "description": "Menu Complet",
                "price": "À partir de 30 DHS",
                "badge": badge,
                "duration": 15,
                "bgEffect": bg_effect,
                "bgColor": bg_color,
                "nameLayout": {"x": 0, "y": -450, "scale": 1.3, "rotation": 0, "animIn": "fadeDown", "delay": 0, "z": 20},
                "descLayout": {"x": 0, "y": -380, "scale": 1, "rotation": 0, "animIn": "fadeUp", "delay": 0.2, "z": 20},
                "priceLayout": {"x": 0, "y": 450, "scale": 1.2, "rotation": 0, "animIn": "zoomIn", "delay": 0.5, "z": 20},
                "badgeLayout": {"x": -600, "y": -450, "scale": 1.2, "rotation": -15, "animIn": "fadeLeft", "delay": 0.4, "z": 30},
                "components": components,
                "tv": "1",
                "isGeneratingIA": False
            }
        }
    }
    with open(os.path.join(menu_dir, filename), 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

# Helper for grid positioning
def generate_grid_components(rows, cols, x_start, y_start, x_gap, y_gap, scale):
    assets_pool = ["bocadillo cheese.png", "sandwiche americain.png", "coca.png", "frite.png"]
    comps = []
    idx = 0
    for r in range(rows):
        for c in range(cols):
            asset = assets_pool[idx % len(assets_pool)]
            x = x_start + (c * x_gap)
            y = y_start + (r * y_gap)
            delay = (r * cols + c) * 0.1
            
            # Add image
            comps.append({
                "type": "main", "assetId": asset, "x": x, "y": y, "scale": scale, 
                "rotation": 0, "z": 10, "animIn": "zoomIn", "animOut": "zoomOut", "delay": delay, "exitTime": 14
            })
            
            # Add price/text label under image using customText if supported, 
            # but since we rely on base customText logic, we will just position them nicely.
            comps.append({
                "type": "customText",
                "content": f"Produit {idx+1}\\n35 DH",
                "x": x,
                "y": y + (120 * scale),
                "scale": 1,
                "color": "#ffffff",
                "fontSize": int(30 * scale),
                "fontFamily": "Inter",
                "hasShadow": True,
                "strokeColor": "#000000",
                "z": 15,
                "animIn": "fadeUp",
                "animOut": "fadeDown",
                "delay": delay + 0.1
            })
            idx += 1
    return comps

# Model 6: 6 Products (2 Rows x 3 Cols)
comp_m6 = generate_grid_components(rows=2, cols=3, x_start=-500, y_start=-150, x_gap=500, y_gap=350, scale=0.8)
create_model("menu_data_model6_1.json", "none", "radial-gradient(circle at 50% 50%, #2a2a2a 0%, #000000 100%)", comp_m6, "NOTRE SÉLECTION (6 ARTICLES)", "PROMO")

# Model 7: 8 Products (2 Rows x 4 Cols)
comp_m7 = generate_grid_components(rows=2, cols=4, x_start=-600, y_start=-150, x_gap=400, y_gap=350, scale=0.6)
create_model("menu_data_model7_1.json", "neon", "#0d0d1a", comp_m7, "GRAND MENU (8 ARTICLES)", "NOUVEAU")

# Model 8: 6 Products (3 Rows x 2 Cols) - Centered with Fire
comp_m8 = generate_grid_components(rows=3, cols=2, x_start=-300, y_start=-200, x_gap=600, y_gap=250, scale=0.7)
create_model("menu_data_model8_1.json", "fire", "radial-gradient(circle at 50% 50%, #4a0000 0%, #000000 100%)", comp_m8, "MENU GRILL (6 ARTICLES)", "HOT")
