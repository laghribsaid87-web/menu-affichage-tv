import json

def sys_coords(x, y):
    return x - 960, y - 350

menu_data = {
  "orientation": "horizontal",
  "theme": "light",
  "colorTheme": {
    "bg": "#ffffff",
    "text": "#000000",
    "primary": "#ff0000",
    "priceBg": "#ff0000",
    "priceBorder": "#cc0000"
  },
  "formules": {
    "formule_1": {
      "id": "formule_1",
      "name": "Design Burger",
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

# 1. Top Left MENU Banner
cx, cy = sys_coords(120, 80)
components.append({
  "type": "shape",
  "shapeType": "rect",
  "x": cx, "y": cy, "width": 450, "height": 130,
  "color": "#ff0000",
  "textColor": "#ffffff",
  "content": "MENU",
  "fontSize": 60,
  "borderRadius": 50,
  "scale": 1, "z": 5
})

# 2. Grid Items (4 columns, 2 rows)
cols_x = [230, 480, 730, 980]
row1_y = 250
row2_y = 520

titles = ["BEEF BURGER", "BEEF BURGER X2", "CHEESE BURGER", "CHEESE BURGER X2", "CHILLI HOT DOG", "CHILLI HOT DOG XL", "CHEESY HOT DOG", "FRENCH FRIES"]
prices = ["$20.00", "$30.00", "$25.00", "$35.00", "$20.00", "$25.00", "$25.00", "$15.00"]
img_placeholders = [
    "burger1.png",
    "burger2.png",
    "burger3.png",
    "burger4.png",
    "hotdog1.png",
    "hotdog2.png",
    "hotdog3.png",
    "fries.png"
]

for i in range(8):
    r = 0 if i < 4 else 1
    c = i % 4
    x = cols_x[c]
    y_base = row1_y if r == 0 else row2_y
    
    img_x, img_y = sys_coords(x, y_base)
    # Image
    components.append({
      "type": "rawImage",
      "url": "https://placehold.co/300x250/transparent/orange?text=Img",
      "x": img_x, "y": img_y, "scale": 0.8, "z": 5
    })
    
    badge_x, badge_y = sys_coords(x - 70, y_base + 80)
    # Number badge (red circle)
    components.append({
      "type": "shape",
      "shapeType": "circle",
      "x": badge_x, "y": badge_y, "width": 30, "height": 30,
      "color": "#ff0000",
      "textColor": "#ffffff",
      "content": str(i+1),
      "fontSize": 18,
      "scale": 1, "z": 6
    })
    
    title_x, title_y = sys_coords(x + 10, y_base + 80)
    # Title
    components.append({
      "type": "customText",
      "x": title_x, "y": title_y, "scale": 1, "z": 5,
      "content": f"<b>{titles[i]}</b>",
      "color": "#000000", "fontSize": 20
    })
    
    price_x, price_y = sys_coords(x + 10, y_base + 115)
    # Price
    components.append({
      "type": "customText",
      "x": price_x, "y": price_y, "scale": 1, "z": 5,
      "content": f"<b>{prices[i]}</b>",
      "color": "#ff0000", "fontSize": 22
    })

# 3. BEVERAGES Banner
banner_x, banner_y = sys_coords(340, 700)
components.append({
  "type": "shape",
  "shapeType": "rect",
  "x": banner_x, "y": banner_y, "width": 680, "height": 55,
  "color": "#222222",
  "isGradient": True,
  "color2": "transparent",
  "gradientAngle": 90,
  "textColor": "#ffffff",
  "content": "<div style='text-align:left; width:100%; padding-left: 40px; font-weight:normal; letter-spacing: 2px;'>BEVERAGES</div>",
  "fontSize": 35,
  "borderRadius": 0,
  "scale": 1, "z": 5
})

# 4. Beverages List (2 columns)
bev1_x, bev1_y = sys_coords(260, 850)
components.append({
  "type": "customText",
  "x": bev1_x, "y": bev1_y, "scale": 1, "z": 5,
  "content": "<div style='line-height: 1.8; font-size:18px; font-weight:bold; color:#555; text-align:left; width:300px;'>☕ NESTEA <span style='float:right; color:red;'>$8</span><br>🍵 GREEN TEA <span style='float:right; color:red;'>$8</span><br>🍊 FRESH ORANGE <span style='float:right; color:red;'>$9</span><br>🧃 KOTAK SOSRO <span style='float:right; color:red;'>$6</span><br>🍋 FRESH MANGO <span style='float:right; color:red;'>$9</span></div>"
})
bev2_x, bev2_y = sys_coords(610, 850)
components.append({
  "type": "customText",
  "x": bev2_x, "y": bev2_y, "scale": 1, "z": 5,
  "content": "<div style='line-height: 1.8; font-size:18px; font-weight:bold; color:#555; text-align:left; width:300px;'>🥤 COCA COLA <span style='float:right; color:red;'>$8</span><br>🟢 SPRITE <span style='float:right; color:red;'>$8</span><br>🟠 FANTA <span style='float:right; color:red;'>$9</span><br>🍫 MILO <span style='float:right; color:red;'>$6</span><br>🍵 TEH BOTOL <span style='float:right; color:red;'>$9</span></div>"
})

# 5. Hero Burger
hero_x, hero_y = sys_coords(1450, 420)
components.append({
  "type": "rawImage",
  "url": "https://placehold.co/900x700/transparent/orange?text=Giant+Hero+Burger",
  "x": hero_x, "y": hero_y, "scale": 1, "z": 5
})
hero_t1_x, hero_t1_y = sys_coords(1450, 710)
components.append({
  "type": "customText",
  "x": hero_t1_x, "y": hero_t1_y, "scale": 1, "z": 5,
  "content": "<b>SPECIAL BURGER X2</b>",
  "color": "#000000", "fontSize": 45
})
hero_t2_x, hero_t2_y = sys_coords(1450, 780)
components.append({
  "type": "customText",
  "x": hero_t2_x, "y": hero_t2_y, "scale": 1, "z": 5,
  "content": "WITH <span style='font-size:45px; font-weight:bold;'>EGG & SMOKED BEEF</span>",
  "color": "#000000", "fontSize": 25
})
hero_t3_x, hero_t3_y = sys_coords(1450, 870)
components.append({
  "type": "customText",
  "x": hero_t3_x, "y": hero_t3_y, "scale": 1, "z": 5,
  "content": "<b>$40.00</b>",
  "color": "#ff0000", "fontSize": 60
})

# 6. Logo Placeholder
logo_x, logo_y = sys_coords(1450, 960)
components.append({
  "type": "customText",
  "x": logo_x, "y": logo_y, "scale": 1, "z": 5,
  "content": "<div style='text-align:center;'><span style='font-family:cursive; font-size:30px;'>The</span><br><b style='color:red; font-size:60px;'>SOPHISTICATE</b><br><span style='font-size:16px; font-weight:bold;'>BURGER FOR THE ELITE</span></div>",
  "color": "#000000", "fontSize": 30
})

# 7. Footer Banner
foot_x, foot_y = sys_coords(550, 1060)
components.append({
  "type": "shape",
  "shapeType": "rect",
  "x": foot_x, "y": foot_y, "width": 1100, "height": 40,
  "color": "#000000",
  "textColor": "#ffffff",
  "content": "Road 032, Marina, Newyork &nbsp;&nbsp;&nbsp; Tel: 000 111 0689 0666, 0882- 111 0689 0666",
  "fontSize": 18,
  "borderRadius": 0,
  "scale": 1, "z": 5
})

with open('menu_data_sophisticate_1.json', 'w', encoding='utf-8') as f:
    json.dump(menu_data, f, indent=2, ensure_ascii=False)
