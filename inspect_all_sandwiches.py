# -*- coding: utf-8 -*-
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

for model in ['menu_model2_urban.html', 'menu_model3_vibrant.html']:
    with open(f'c:/Users/pc/Desktop/menu/{model}', 'r', encoding='utf-8') as f:
        text = f.read()
    print("=== MODEL:", model, "===")
    nums = re.findall(r'(\d+)\s*<span>\s*DH\s*</span>', text, re.IGNORECASE)
    print("Prices found:", nums[:15])
