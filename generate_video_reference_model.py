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

def create_model(filename, components):
    data = {
        "assets": base_assets,
        "orientation": "horizontal",
        "formules": {
            "formule_main": {
                "name": "",
                "description": "",
                "price": "",
                "badge": "",
                "duration": 20,
                "bgEffect": "none",
                "bgColor": "vid.mp4",
                "nameLayout": None,
                "descLayout": None,
                "priceLayout": None,
                "badgeLayout": None,
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
    assets_pool = ["bocadillo cheese.png", "sandwiche americain.png", "bocadillo cheese.png", "sandwiche americain.png", "bocadillo cheese.png"]
    
    # Bottom area background (Translucent Black)
    comps.append({
         "type": "shape",
         "shapeType": "rectangle",
         "x": 0, "y": 540,
         "width": 1920, "height": 380,
         "color": "#000000", "isGradient": False,
         "z": 1, "opacity": 0.6,
         "animIn": "fadeUp", "delay": 0
    })

    x_positions = [-700, -350, 0, 350, 700]
    y_img = 470
    y_text = 580
    y_price = 650
    scale_img = 0.45

    for i in range(5):
        asset = assets_pool[i]
        x = x_positions[i]
        delay = 0.5 + (i * 0.1)
        
        comps.append({
            "type": "main", "assetId": asset, "x": x, "y": y_img, "scale": scale_img, 
            "rotation": 0, "z": 10, "animIn": "zoomIn", "animOut": "zoomOut", "delay": delay, "exitTime": 19
        })
        
        comps.append({
            "type": "customText",
            "content": f"MENU {i+1}",
            "x": x,
            "y": y_text,
            "scale": 1,
            "color": "#ffffff",
            "fontSize": 26,
            "fontFamily": "'Inter', sans-serif",
            "fontWeight": "bold",
            "hasShadow": True,
            "z": 15,
            "animIn": "fadeUp",
            "animOut": "fadeDown",
            "delay": delay + 0.1
        })

        comps.append({
            "type": "shape",
            "shapeType": "pill",
            "x": x, "y": y_price,
            "width": 100, "height": 40,
            "color": "#e74c3c" if i % 2 == 0 else "#222222",
            "z": 12, "opacity": 1,
            "animIn": "zoomIn", "delay": delay + 0.2
        })
        
        comps.append({
            "type": "customText",
            "content": f"{5.50 + i}€",
            "x": x,
            "y": y_price,
            "scale": 1,
            "color": "#ffffff",
            "fontSize": 22,
            "fontFamily": "Impact, sans-serif",
            "fontWeight": "bold",
            "z": 15,
            "animIn": "zoomIn",
            "animOut": "zoomOut",
            "delay": delay + 0.2
        })

    return comps

comp_m10 = []

# Glowing Divider Line
comp_m10.append({
     "type": "shape",
     "shapeType": "rectangle",
     "x": 0, "y": 350,
     "width": 1920, "height": 4,
     "color": "#00d2ff", "isGradient": False,
     "z": 50, "opacity": 1,
     "animIn": "fadeIn", "delay": 0.3
})

# Divider text
comp_m10.append({
    "type": "customText",
    "content": "www.menuboard-dynamique.fr",
    "x": 0,
    "y": 350,
    "scale": 1,
    "color": "#ffffff",
    "fontSize": 22,
    "fontFamily": "'Inter', sans-serif",
    "fontWeight": "bold",
    "hasShadow": True,
    "z": 51,
    "animIn": "fadeIn",
    "delay": 0.4
})

# Top Showcase
comp_m10.extend([
    {"type": "main", "assetId": "coca.png", "x": -450, "y": 50, "scale": 1.1, "rotation": -5, "z": 8, "animIn": "slideInLeft", "animOut": "zoomOut", "delay": 0.2},
    {"type": "main", "assetId": "frite.png", "x": -150, "y": 50, "scale": 0.9, "rotation": 5, "z": 7, "animIn": "slideInUp", "animOut": "zoomOut", "delay": 0.3},
    {"type": "main", "assetId": "sandwiche americain.png", "x": 350, "y": 50, "scale": 1.4, "rotation": 0, "z": 10, "animIn": "slideInRight", "animOut": "zoomOut", "delay": 0.1, "continuousAnim": "pulse"}
])

# Custom Title and Price (replacing hardcoded Layouts)
comp_m10.extend([
    {"type": "customText", "content": "CHEESE BURGER", "x": 100, "y": -220, "scale": 1, "rotation": -2, "color": "#ffffff", "fontSize": 140, "fontFamily": "Impact, sans-serif", "hasShadow": True, "z": 20, "animIn": "bounceIn", "delay": 0},
    {"type": "shape", "shapeType": "circle", "x": -250, "y": -120, "width": 160, "height": 160, "color": "#e74c3c", "z": 19, "opacity": 1, "animIn": "zoomIn", "delay": 0.4},
    {"type": "customText", "content": "5.50€", "x": -250, "y": -120, "scale": 1, "rotation": 0, "color": "#ffeb3b", "fontSize": 45, "fontFamily": "Impact, sans-serif", "hasShadow": True, "z": 20, "animIn": "zoomIn", "delay": 0.5},
    {"type": "shape", "shapeType": "burst", "x": -600, "y": -180, "width": 150, "height": 150, "color": "#e74c3c", "z": 29, "opacity": 1, "animIn": "zoomIn", "delay": 0.3},
    {"type": "customText", "content": "NOUVEAU", "x": -600, "y": -180, "scale": 1, "rotation": 0, "color": "#ffffff", "fontSize": 35, "fontFamily": "'Oswald', sans-serif", "hasShadow": True, "z": 30, "animIn": "zoomIn", "delay": 0.4}
])

comp_m10.extend(generate_bottom_row())

create_model("menu_data_video_1.json", comp_m10)

print("Generated menu_data_video_1.json successfully!")
