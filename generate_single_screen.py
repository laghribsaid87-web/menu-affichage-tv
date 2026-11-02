import json
import uuid

target_file = 'menu_data_smart_1.json'
menu_data = {"formules": {}}

# Load data
try:
    with open('config_dynamic.json', 'r', encoding='utf-8') as f:
        dynamic_data = json.load(f)
    bocadillos = dynamic_data.get("bocadillos", [])
except:
    bocadillos = []

if len(bocadillos) < 4:
    bocadillos = [
        {"name": "BOCADILLO CHEESE", "price": "24", "img": "processed_images/bocadillo cheese 24 dh.png"},
        {"name": "BOCADILLO COMPLET", "price": "29", "img": "processed_images/bocadillo complet 29 dh.png"},
        {"name": "BOCADILLO TANGEROIS", "price": "24", "img": "processed_images/bocadillo tangerois 24 dh.png"},
        {"name": "BOCADILLO THON", "price": "22", "img": "processed_images/bocadillo thon 22 dh.png"}
    ]

f_key = f"formule_smart_{uuid.uuid4().hex[:6]}"
formule = {
    "name": " ", # Space so it doesn't render huge text
    "tv": "1",
    "duration": 10,
    "components": []
}

# 1. Dark Background Shape (Center 0,0)
formule["components"].append({
    "type": "shape",
    "shapeType": "rect",
    "width": 1920,
    "height": 1080,
    "color": "#000000",
    "opacity": 1,
    "borderRadius": 0,
    "x": 0,
    "y": 0,
    "scale": 1.1, # Slightly larger to cover edges
    "z": 0,
    "animIn": "fadeIn",
    "animOut": "fadeOut",
    "delay": 0,
    "rotation": 0
})

# 2. Top Header Ribbon (Top Center: Y = -450)
formule["components"].append({
    "type": "shape",
    "shapeType": "rect",
    "width": 600,
    "height": 80,
    "color": "#dc2626",
    "opacity": 1,
    "borderRadius": 10,
    "x": 0,
    "y": -460,
    "scale": 1,
    "z": 2,
    "animIn": "fadeIn",
    "animOut": "fadeOut",
    "delay": 0,
    "rotation": 0
})

formule["components"].append({
    "type": "customText",
    "content": "NOS BOCADILLOS",
    "x": 0,
    "y": -460,
    "scale": 1.5, # Canvas uses scale for font size
    "z": 15,
    "animIn": "fadeIn",
    "animOut": "fadeOut",
    "delay": 0,
    "rotation": 0,
    "color": "#ffffff",
    "fontFamily": "'Montserrat', sans-serif"
})

# 3. 4 Items (Top Half: Y = -150)
# X positions for 4 items: -600, -200, 200, 600
x_positions = [-650, -220, 220, 650]
for i in range(4):
    item = bocadillos[i]
    x_pos = x_positions[i]
    base_y = -150

    # Fries (Behind)
    formule["components"].append({
        "type": "rawImage",
        "url": "processed_images/cornet1.png",
        "x": x_pos + 80,
        "y": base_y - 60,
        "scale": 1,
        "z": 10,
        "animIn": "fadeIn",
        "animOut": "fadeOut",
        "delay": 0.2,
        "rotation": 0
    })

    # Sandwich
    formule["components"].append({
        "type": "rawImage",
        "url": item["img"],
        "x": x_pos - 20,
        "y": base_y,
        "scale": 0.6,
        "z": 20,
        "animIn": "zoomIn",
        "animOut": "fadeOut",
        "delay": 0.3,
        "rotation": -5
    })

    # Name
    formule["components"].append({
        "type": "customText",
        "content": item["name"],
        "x": x_pos,
        "y": base_y + 120,
        "scale": 0.9,
        "z": 15,
        "animIn": "fadeIn",
        "animOut": "fadeOut",
        "delay": 0.4,
        "rotation": 0,
        "color": "#ffffff",
        "fontFamily": "'Oswald', sans-serif"
    })

    # Price
    formule["components"].append({
        "type": "customText",
        "content": f"{item['price']} DH",
        "x": x_pos,
        "y": base_y + 180,
        "scale": 1.4,
        "z": 25,
        "animIn": "zoomIn",
        "animOut": "fadeOut",
        "delay": 0.5,
        "rotation": 0,
        "color": "#facc15",
        "fontFamily": "'Oswald', sans-serif"
    })

# 4. Bottom Spotlight (Bottom Half: Y = 280)
spotlight_item = bocadillos[3]

# Big Red Box
formule["components"].append({
    "type": "shape",
    "shapeType": "rect",
    "width": 1400,
    "height": 380,
    "color": "#b91c1c",
    "opacity": 1,
    "borderRadius": 30,
    "x": 0,
    "y": 300,
    "scale": 1,
    "z": 5,
    "animIn": "slideInUp",
    "animOut": "fadeOut",
    "delay": 0.8,
    "rotation": 0
})

# Yellow Badge
formule["components"].append({
    "type": "shape",
    "shapeType": "rect",
    "width": 300,
    "height": 50,
    "color": "#facc15",
    "opacity": 1,
    "borderRadius": 25,
    "x": -400,
    "y": 200,
    "scale": 1,
    "z": 6,
    "animIn": "fadeIn",
    "animOut": "fadeOut",
    "delay": 1.0,
    "rotation": -3
})
formule["components"].append({
    "type": "customText",
    "content": "LE CHOIX DU CHEF",
    "x": -400,
    "y": 200,
    "scale": 0.8,
    "z": 15,
    "animIn": "fadeIn",
    "animOut": "fadeOut",
    "delay": 1.0,
    "rotation": -3,
    "color": "#000000",
    "fontFamily": "'Oswald', sans-serif"
})

# Spotlight Title
formule["components"].append({
    "type": "customText",
    "content": spotlight_item["name"],
    "x": -350,
    "y": 280,
    "scale": 2.5,
    "z": 15,
    "animIn": "fadeIn",
    "animOut": "fadeOut",
    "delay": 1.1,
    "rotation": 0,
    "color": "#ffffff",
    "fontFamily": "'Montserrat', sans-serif"
})

# Spotlight Price
formule["components"].append({
    "type": "customText",
    "content": f"{spotlight_item['price']} DH",
    "x": -350,
    "y": 420,
    "scale": 4.0,
    "z": 15,
    "animIn": "zoomIn",
    "animOut": "fadeOut",
    "delay": 1.2,
    "rotation": 0,
    "color": "#ffffff",
    "fontFamily": "'Montserrat', sans-serif"
})

# Spotlight Fries
formule["components"].append({
    "type": "rawImage",
    "url": "processed_images/cornet1.png",
    "x": 350,
    "y": 250,
    "scale": 1.5,
    "z": 18,
    "animIn": "fadeIn",
    "animOut": "fadeOut",
    "delay": 1.3,
    "rotation": 0
})

# Spotlight Sandwich
formule["components"].append({
    "type": "rawImage",
    "url": spotlight_item["img"],
    "x": 250,
    "y": 300,
    "scale": 1.8,
    "z": 20,
    "animIn": "zoomIn",
    "animOut": "fadeOut",
    "delay": 1.4,
    "rotation": -10
})

menu_data["formules"] = {f_key: formule}
with open(target_file, 'w', encoding='utf-8') as f:
    json.dump(menu_data, f, indent=2, ensure_ascii=False)
print("Regenerated accurately with center-based coordinates!")
