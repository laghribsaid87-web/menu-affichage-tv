import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

models = ['menu_model1_emirates.html', 'menu_model2_urban.html', 'menu_model3_vibrant.html']

for m in models:
    with open(f"c:/Users/pc/Desktop/menu/{m}", "r", encoding="utf-8") as f:
        html = f.read()
    
    print("="*40, m, "="*40)
    # Search for complet card price
    # Let's find the first occurrence of 29 in the file
    idx = html.find("29")
    if idx != -1:
        snippet = html[max(0, idx-150): min(len(html), idx+250)]
        print("SAMPLE SNIPPET:\n", snippet)
