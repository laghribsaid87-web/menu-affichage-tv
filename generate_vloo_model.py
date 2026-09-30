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
                "nameLayout": {"x": 0, "y": -420, "scale": 1.4, "rotation": 0, "animIn": "fadeDown", "delay": 0, "z": 20},
                "descLayout": {"x": 0, "y": -350, "scale": 1, "rotation": 0, "animIn": "fadeUp", "delay": 0.2, "z": 20},
                # Hide default price to use custom badge price
                "priceLayout": {"x": 0, "y": -1000, "scale": 0, "rotation": 0, "animIn": "zoomIn", "delay": 0.5, "z": 0},
                "badgeLayout": {"x": 0, "y": -1000, "scale": 0, "rotation": 0, "animIn": "fadeLeft", "delay": 0.4, "z": 0},
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
    
    # Elegant dark glass banner for bottom row
    comps.append({
         "type": "shape",
         "shapeType": "badge",
         "x": 0, "y": 380,
         "width": 1920, "height": 300,
         "color": "#000000", "color2": "#1a1a1a", "isGradient": True,
         "z": 1, "opacity": 0.85,
         "animIn": "fadeUp", "delay": 0
    })

    # Exact non-overlapping coordinates for 6 items
    x_positions = [-750, -450, -150, 150, 450, 750]
    y_img = 300
    y_text = 430
    scale_img = 0.35  

    for i in range(6):
        asset = assets_pool[i % len(assets_pool)]
        x = x_positions[i]
        delay = i * 0.1
        
        comps.append({
            "type": "main", "assetId": asset, "x": x, "y": y_img, "scale": scale_img, 
            "rotation": 0, "z": 10, "animIn": "zoomIn", "animOut": "zoomOut", "delay": delay, "exitTime": 19
        })
        
        # Title of small item
        comps.append({
            "type": "customText",
            "content": f"Burger {i+1}",
            "x": x,
            "y": y_text,
            "scale": 1,
            "color": "#ffffff",
            "fontSize": 24,
            "fontFamily": "Inter",
            "hasShadow": True,
            "strokeColor": "#000000",
            "z": 15,
            "animIn": "fadeUp",
            "animOut": "fadeDown",
            "delay": delay + 0.1
        })
        
        # Price of small item in yellow
        comps.append({
            "type": "customText",
            "content": "25 DH",
            "x": x,
            "y": y_text + 40,
            "scale": 1,
            "color": "#ffd700",
            "fontSize": 26,
            "fontFamily": "Inter",
            "hasShadow": True,
            "strokeColor": "#000000",
            "z": 15,
            "animIn": "fadeUp",
            "animOut": "fadeDown",
            "delay": delay + 0.2
        })
    return comps

comp_vloo = []

# Top Section (Hero) 
# Drink
comp_vloo.append({"type": "main", "assetId": "coca.png", "x": -350, "y": -100, "scale": 1.2, "rotation": -5, "z": 8, "animIn": "fadeLeft", "animOut": "zoomOut", "delay": 0.4})
# Fries
comp_vloo.append({"type": "main", "assetId": "frite.png", "x": 350, "y": -80, "scale": 1.1, "rotation": 5, "z": 9, "animIn": "fadeRight", "animOut": "zoomOut", "delay": 0.2})
# Main Burger
comp_vloo.append({"type": "main", "assetId": "sandwiche americain.png", "x": 0, "y": -120, "scale": 1.8, "rotation": 0, "z": 10, "animIn": "zoomIn", "animOut": "zoomOut", "delay": 0, "continuousAnim": "glow"})

# Giant Price Badge (Vloo style)
comp_vloo.append({
     "type": "shape",
     "shapeType": "badge",
     "x": -450, "y": -280,
     "width": 180, "height": 180,
     "color": "#d32f2f", "color2": "#b71c1c", "isGradient": True,
     "z": 20, "opacity": 1,
     "animIn": "zoomIn", "delay": 0.6, "borderRadius": 90
})
comp_vloo.append({
    "type": "customText",
    "content": "45\\nDH",
    "x": -450, "y": -290,
    "scale": 1,
    "color": "#ffffff",
    "fontSize": 48,
    "fontFamily": "Inter",
    "hasShadow": True,
    "strokeColor": "#000000",
    "z": 25,
    "animIn": "zoomIn", "delay": 0.7
})

# Custom Promo Badge on right side
comp_vloo.append({
     "type": "shape",
     "shapeType": "badge",
     "x": 450, "y": -350,
     "width": 200, "height": 60,
     "color": "#ffd700", "color2": "#ffb300", "isGradient": True,
     "z": 20, "opacity": 1,
     "animIn": "fadeRight", "delay": 0.6, "borderRadius": 10
})
comp_vloo.append({
    "type": "customText",
    "content": "NOUVEAU",
    "x": 450, "y": -345,
    "scale": 1,
    "color": "#000000",
    "fontSize": 30,
    "fontFamily": "Inter",
    "hasShadow": False,
    "strokeColor": "#ffffff",
    "z": 25,
    "animIn": "fadeRight", "delay": 0.7
})

# Bottom row
comp_vloo.extend(generate_bottom_row())

wood_bg_url = "url('https://images.unsplash.com/photo-1546484396-fb3fc6f95f98?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80') center/cover no-repeat"

create_model("menu_data_model_vloo_1.json", "smoke", wood_bg_url, comp_vloo, "LE BÛCHERON", "0")
