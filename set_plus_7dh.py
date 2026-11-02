# -*- coding: utf-8 -*-
"""
Update all 3 models so that Chip 2 literally displays '+7 DH' instead of calculated totals:
- Chip 1: Sandwich price (e.g. 29 DH, 30 DH, 35 DH...)
- Chip 2: 🥤 + BOISSON  |  +7 DH
"""

import re
import os

MODELS = [
    r'c:\Users\pc\Desktop\menu\menu_model1_emirates.html',
    r'c:\Users\pc\Desktop\menu\menu_model2_urban.html',
    r'c:\Users\pc\Desktop\menu\menu_model3_vibrant.html'
]

def update_file(path):
    print("Updating to literal +7 DH:", os.path.basename(path))
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Model 1 Emirates
    # <span class="label">🥤 + BOISSON (+7DH)</span>\s*<span class="num">\d+<span class="curr">DH</span></span>
    # Or previous variants
    content = re.sub(
        r'<span class="label">🥤[^<]*</span>\s*<span class="num">[^<]*<span class="curr">DH</span></span>',
        r'<span class="label">🥤 + BOISSON</span>\n<span class="num">+7<span class="curr">DH</span></span>',
        content
    )

    # 2. Model 2 Urban
    # <span class="p-label">🥤[^<]*</span>\s*<span class="p-val">[^<]*<span>DH</span></span>
    content = re.sub(
        r'<span class="p-label">🥤[^<]*</span>\s*<span class="p-val">[^<]*<span>DH</span></span>',
        r'<span class="p-label">🥤 + Boisson</span>\n<span class="p-val">+7<span>DH</span></span>',
        content
    )

    # 3. Model 3 Vibrant
    # <span class="p-tag">🥤[^<]*</span>\s*<span class="p-number">[^<]*<span>DH</span></span>
    content = re.sub(
        r'<span class="p-tag">🥤[^<]*</span>\s*<span class="p-number">[^<]*<span>DH</span></span>',
        r'<span class="p-tag">🥤 + Boisson</span>\n<span class="p-number">+7<span>DH</span></span>',
        content
    )

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated", os.path.basename(path))

for p in MODELS:
    update_file(p)

print("All 3 models updated to display '+7 DH' on Chip 2!")

