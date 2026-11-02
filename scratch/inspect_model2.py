import sys
sys.stdout.reconfigure(encoding='utf-8')

with open("c:/Users/pc/Desktop/menu/menu_model2_urban.html", "r", encoding="utf-8") as f:
    html = f.read()

idx = html.find("urban-card")
if idx != -1:
    print(html[idx: idx+800])

