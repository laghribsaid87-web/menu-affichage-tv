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
                "description": "Une sélection premium pour les gourmands",
                "price": "45 DHS",
                "badge": badge,
                "duration": 10,
                "bgEffect": bg_effect,
                "bgColor": bg_color,
                "nameLayout": {"x": 0, "y": -400, "scale": 1.5, "rotation": 0, "animIn": "fadeDown", "delay": 0, "z": 20},
                "descLayout": {"x": 0, "y": -330, "scale": 1.2, "rotation": 0, "animIn": "fadeUp", "delay": 0.2, "z": 20},
                "priceLayout": {"x": 0, "y": 400, "scale": 2, "rotation": 0, "animIn": "zoomIn", "delay": 0.5, "z": 20},
                "badgeLayout": {"x": -450, "y": -400, "scale": 1.5, "rotation": -15, "animIn": "fadeLeft", "delay": 0.4, "z": 30},
                "components": components,
                "tv": "1",
                "isGeneratingIA": False
            }
        }
    }
    with open(os.path.join(menu_dir, filename), 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

# Model 1: Spicy Fire (Burger / Tacos theme)
comp_m1 = [
    {"type": "main", "assetId": "bocadillo cheese.png", "x": -250, "y": 0, "scale": 1.5, "rotation": -5, "z": 10, "animIn": "fadeLeft", "animOut": "zoomOut", "delay": 0, "exitTime": 9, "continuousAnim": "pulse"},
    {"type": "main", "assetId": "sandwiche americain.png", "x": 250, "y": 50, "scale": 1.3, "rotation": 5, "z": 9, "animIn": "fadeRight", "animOut": "zoomOut", "delay": 0.2, "exitTime": 9},
    {"type": "main", "assetId": "frite.png", "x": 0, "y": 200, "scale": 1.2, "rotation": 0, "z": 15, "animIn": "zoomIn", "animOut": "fadeDown", "delay": 0.4, "exitTime": 9},
    {"type": "main", "assetId": "coca.png", "x": -450, "y": 150, "scale": 1, "rotation": -10, "z": 5, "animIn": "fadeUp", "animOut": "fadeLeft", "delay": 0.6, "exitTime": 9}
]
create_model("menu_data_model1_1.json", "fire", "radial-gradient(circle at 50% 50%, #8b0000 0%, #1a0000 100%)", comp_m1, "MENU SPICY 🔥", "HOT!")

# Model 2: Fresh Cafe (Steam effect)
comp_m2 = [
    {"type": "main", "assetId": "coca.png", "x": 0, "y": 50, "scale": 1.8, "rotation": 0, "z": 10, "animIn": "zoomIn", "animOut": "zoomOut", "delay": 0, "exitTime": 9, "continuousAnim": "glow"},
    {"type": "main", "assetId": "bocadillo cheese.png", "x": -350, "y": 150, "scale": 1.1, "rotation": -15, "z": 8, "animIn": "fadeLeft", "animOut": "zoomOut", "delay": 0.3, "exitTime": 9},
    {"type": "main", "assetId": "frite.png", "x": 350, "y": 150, "scale": 1.1, "rotation": 15, "z": 8, "animIn": "fadeRight", "animOut": "zoomOut", "delay": 0.3, "exitTime": 9}
]
create_model("menu_data_model2_1.json", "steam", "linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%)", comp_m2, "MENU FRESH 🍃", "NOUVEAU")

# Model 3: Neon Cyberpunk (Neon effect)
comp_m3 = [
    {"type": "main", "assetId": "sandwiche americain.png", "x": 0, "y": -50, "scale": 1.6, "rotation": 0, "z": 10, "animIn": "fadeDown", "animOut": "fadeUp", "delay": 0.1, "exitTime": 9, "continuousAnim": "pulse"},
    {"type": "main", "assetId": "coca.png", "x": -300, "y": 100, "scale": 1.2, "rotation": -5, "z": 9, "animIn": "fadeLeft", "animOut": "fadeLeft", "delay": 0.4, "exitTime": 9},
    {"type": "main", "assetId": "coca.png", "x": 300, "y": 100, "scale": 1.2, "rotation": 5, "z": 9, "animIn": "fadeRight", "animOut": "fadeRight", "delay": 0.4, "exitTime": 9}
]
create_model("menu_data_model3_1.json", "neon", "#0a0a0a", comp_m3, "CYBER BITE ⚡", "PROMO")

# Model 4: Elegant Minimal (Snow/Chalk effect, subtle)
comp_m4 = [
    {"type": "main", "assetId": "bocadillo cheese.png", "x": 0, "y": 0, "scale": 1.4, "rotation": 0, "z": 10, "animIn": "zoomIn", "animOut": "zoomOut", "delay": 0, "exitTime": 9},
    {"type": "main", "assetId": "frite.png", "x": 200, "y": 180, "scale": 0.9, "rotation": 10, "z": 15, "animIn": "fadeUp", "animOut": "fadeDown", "delay": 0.5, "exitTime": 9},
    {"type": "main", "assetId": "coca.png", "x": -200, "y": 150, "scale": 0.9, "rotation": -5, "z": 5, "animIn": "fadeUp", "animOut": "fadeDown", "delay": 0.7, "exitTime": 9}
]
create_model("menu_data_model4_1.json", "snow", "radial-gradient(circle at top, #2b5876 0%, #4e4376 100%)", comp_m4, "PREMIUM MENU ⭐", "BEST SELLER")

# Model 5: Ocean / Bubbles 
comp_m5 = [
    {"type": "main", "assetId": "sandwiche americain.png", "x": -200, "y": 50, "scale": 1.5, "rotation": -10, "z": 10, "animIn": "fadeLeft", "animOut": "fadeLeft", "delay": 0, "exitTime": 9, "continuousAnim": "pulse"},
    {"type": "main", "assetId": "frite.png", "x": -450, "y": 200, "scale": 1, "rotation": -20, "z": 15, "animIn": "fadeUp", "animOut": "fadeDown", "delay": 0.3, "exitTime": 9},
    {"type": "main", "assetId": "coca.png", "x": 250, "y": -50, "scale": 1.8, "rotation": 5, "z": 5, "animIn": "zoomIn", "animOut": "fadeRight", "delay": 0.5, "exitTime": 9, "continuousAnim": "glow"}
]
create_model("menu_data_model5_1.json", "bubbles", "linear-gradient(to right, #141e30, #243b55)", comp_m5, "OCEAN MENU 🌊", "FRESH")
