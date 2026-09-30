import json

def sys_coords(x, y):
    return x - 540, y - 350

menu_data = {
  "orientation": "vertical",
  "theme": "light",
  "colorTheme": {
    "bg": "#ffffff",
    "text": "#000000",
    "primary": "#d1121d",
    "priceBg": "#d1121d",
    "priceBorder": "#b00d17"
  },
  "formules": {
    "formule_1": {
      "id": "formule_1",
      "name": "Cooking Master",
      "description": "",
      "price": "",
      "badge": "",
      "duration": 20,
      "bgColor": "#ffffff",
      "isBgNeon": False,
      "nameLayout": { "x": -1000, "y": -1000, "scale": 1, "z": 2 },
      "descLayout": { "x": -1000, "y": -1000, "scale": 1, "z": 2 },
      "priceLayout": { "x": -1000, "y": -1000, "scale": 1, "z": 2 },
      "badgeLayout": { "x": -1000, "y": -1000, "scale": 1, "z": 2 },
      "components": []
    }
  },
  "sequence": ["formule_1"]
}

components = menu_data["formules"]["formule_1"]["components"]

# 1. Giant Red Curve Background
cx, cy = sys_coords(1200, -800)
components.append({
  "type": "shape",
  "shapeType": "circle",
  "x": cx, "y": cy, "width": 3500, "height": 3000,
  "color": "#d1121d",
  "textColor": "transparent",
  "content": "",
  "fontSize": 10,
  "scale": 1, "z": 1
})

# 2. Logo
logox, logoy = sys_coords(200, 100)
components.append({
  "type": "customText",
  "x": logox, "y": logoy, "scale": 1, "z": 5,
  "content": "<div style='font-family:cursive; color:white; font-size:60px;'>Cooking <span style='font-family:sans-serif; font-size:30px; font-weight:bold; display:block; text-align:center;'>MASTER</span></div>",
  "color": "#ffffff"
})

# --- ITEM 1: ROLLER BOX ---

# Product 1 Image
img1x, img1y = sys_coords(400, 550)
components.append({
  "type": "rawImage",
  "url": "https://placehold.co/600x500/transparent/orange?text=Img",
  "x": img1x, "y": img1y, "scale": 1.2, "z": 5
})

# Label "ROLLER BOX"
lbl1x, lbl1y = sys_coords(400, 780)
components.append({
  "type": "shape",
  "shapeType": "rect",
  "x": lbl1x, "y": lbl1y, "width": 550, "height": 100,
  "color": "#b00d17",
  "textColor": "#ffffff",
  "content": "ROLLER BOX",
  "fontSize": 60,
  "rotation": -5,
  "scale": 1, "z": 6
})

# Number 1
n1x, n1y = sys_coords(600, 200)
components.append({
  "type": "shape",
  "shapeType": "rect",
  "x": n1x, "y": n1y, "width": 80, "height": 140,
  "color": "#ffffff",
  "textColor": "#d1121d",
  "content": "1",
  "fontSize": 100,
  "scale": 1, "z": 5
})

# Details 1
d1x, d1y = sys_coords(780, 200)
components.append({
  "type": "customText",
  "x": d1x, "y": d1y, "scale": 1, "z": 5,
  "content": "<div style='color:white; font-size:35px; font-weight:bold; line-height:1.2; text-align:left;'>WRAP<br>CHICKEN FRY<br>FRIES<br>DRINKS</div>"
})

# Line separator
sep1x, sep1y = sys_coords(920, 200)
components.append({
  "type": "shape",
  "shapeType": "rect",
  "x": sep1x, "y": sep1y, "width": 5, "height": 160,
  "color": "#ffffff",
  "textColor": "transparent",
  "content": "",
  "scale": 1, "z": 5
})

# Price 1
p1x, p1y = sys_coords(1050, 200)
components.append({
  "type": "customText",
  "x": p1x, "y": p1y, "scale": 1, "z": 5,
  "content": "<div style='color:white; font-size:65px; font-weight:900;'>$20.99</div>"
})

# Promo Badge 1
b1x, b1y = sys_coords(850, 400)
components.append({
  "type": "shape",
  "shapeType": "circle",
  "x": b1x, "y": b1y, "width": 180, "height": 180,
  "color": "#ffffff",
  "textColor": "#d1121d",
  "content": "SAVE<br>20%",
  "fontSize": 40,
  "scale": 1, "z": 5
})

# --- ITEM 2: BIG BOX MEAL ---

# Product 2 Image
img2x, img2y = sys_coords(700, 1300)
components.append({
  "type": "rawImage",
  "url": "https://placehold.co/600x500/transparent/orange?text=Img",
  "x": img2x, "y": img2y, "scale": 1.2, "z": 5
})

# Label "BIG BOX MEAL"
lbl2x, lbl2y = sys_coords(700, 1600)
components.append({
  "type": "shape",
  "shapeType": "rect",
  "x": lbl2x, "y": lbl2y, "width": 600, "height": 160,
  "color": "#e0e0e0",
  "textColor": "#000000",
  "content": "<div style='font-size:70px; font-weight:900; line-height:1;'>BIG BOX<br><span style='color:#d1121d; font-size:45px;'>MEAL</span></div>",
  "fontSize": 60,
  "scale": 1, "z": 4
})

# Red Stripes on Box
str1x, str1y = sys_coords(850, 1600)
components.append({
  "type": "shape",
  "shapeType": "rect",
  "x": str1x, "y": str1y, "width": 30, "height": 160,
  "color": "#d1121d", "content": "", "scale": 1, "z": 5
})
str2x, str2y = sys_coords(920, 1600)
components.append({
  "type": "shape",
  "shapeType": "rect",
  "x": str2x, "y": str2y, "width": 30, "height": 160,
  "color": "#d1121d", "content": "", "scale": 1, "z": 5
})
str3x, str3y = sys_coords(990, 1600)
components.append({
  "type": "shape",
  "shapeType": "rect",
  "x": str3x, "y": str3y, "width": 30, "height": 160,
  "color": "#d1121d", "content": "", "scale": 1, "z": 5
})

# Number 2
n2x, n2y = sys_coords(150, 1450)
components.append({
  "type": "shape",
  "shapeType": "rect",
  "x": n2x, "y": n2y, "width": 80, "height": 140,
  "color": "#d1121d",
  "textColor": "#ffffff",
  "content": "2",
  "fontSize": 100,
  "scale": 1, "z": 5
})

# Details 2
d2x, d2y = sys_coords(330, 1450)
components.append({
  "type": "customText",
  "x": d2x, "y": d2y, "scale": 1, "z": 5,
  "content": "<div style='color:black; font-size:35px; font-weight:bold; line-height:1.2; text-align:left;'>BURGER<br>FRIED RICE<br>FRENCH FRIES<br>DRINKS</div>"
})

# Line separator 2
sep2x, sep2y = sys_coords(500, 1450)
components.append({
  "type": "shape",
  "shapeType": "rect",
  "x": sep2x, "y": sep2y, "width": 5, "height": 160,
  "color": "#000000",
  "textColor": "transparent",
  "content": "",
  "scale": 1, "z": 5
})

# Price 2
p2x, p2y = sys_coords(620, 1450)
components.append({
  "type": "customText",
  "x": p2x, "y": p2y, "scale": 1, "z": 5,
  "content": "<div style='color:black; font-size:65px; font-weight:900;'>$24.99</div>"
})

# Promo Badge 2
b2x, b2y = sys_coords(400, 1100)
components.append({
  "type": "shape",
  "shapeType": "circle",
  "x": b2x, "y": b2y, "width": 180, "height": 180,
  "color": "#d1121d",
  "textColor": "#ffffff",
  "content": "SAVE<br>30%",
  "fontSize": 40,
  "scale": 1, "z": 5
})

# Footer elements
f1x, f1y = sys_coords(100, 1850)
components.append({
  "type": "shape",
  "shapeType": "rect",
  "x": f1x, "y": f1y, "width": 200, "height": 60,
  "color": "#d1121d", "content": "", "scale": 1, "z": 5
})
f2x, f2y = sys_coords(240, 1850)
components.append({
  "type": "shape",
  "shapeType": "rect",
  "x": f2x, "y": f2y, "width": 20, "height": 60,
  "color": "#d1121d", "content": "", "scale": 1, "z": 5
})
f3x, f3y = sys_coords(280, 1850)
components.append({
  "type": "shape",
  "shapeType": "rect",
  "x": f3x, "y": f3y, "width": 20, "height": 60,
  "color": "#d1121d", "content": "", "scale": 1, "z": 5
})

with open('menu_data_cookingmaster_1.json', 'w', encoding='utf-8') as f:
    json.dump(menu_data, f, indent=2, ensure_ascii=False)
