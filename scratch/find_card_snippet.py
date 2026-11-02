import sys
sys.stdout.reconfigure(encoding='utf-8')

for m in ['menu_model1_emirates.html', 'menu_model2_urban.html', 'menu_model3_vibrant.html']:
    with open(f"c:/Users/pc/Desktop/menu/{m}", "r", encoding="utf-8") as f:
        html = f.read()
    print("="*30, m, "="*30)
    # Find card with complet
    idx = html.find("COMPLET")
    while idx != -1 and "title" not in html[max(0, idx-50): idx+50].lower():
        idx = html.find("COMPLET", idx+1)
    if idx != -1:
        start = html.rfind("<div class=\"", 0, idx)
        print(html[start: start+700])

