import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

for m in ['menu_model1_emirates.html', 'menu_model2_urban.html']:
    with open(f"c:/Users/pc/Desktop/menu/{m}", "r", encoding="utf-8") as f:
        html = f.read()
    print("="*40, m, "="*40)
    for kw in ['price-chalkboard', 'urban-price-box']:
        idx = html.find(kw)
        if idx != -1:
            snippet = html[idx: idx+400]
            print(f"[{kw}]:\n", snippet)
            break

