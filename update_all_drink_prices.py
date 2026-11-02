# -*- coding: utf-8 -*-
"""
Update Drink Prices and Labels across all 3 models:
- Base Sandwich includes Frites
- Adding a Boisson (Monada) is +7 DH (instead of +10 DH)
- Update 29/39 -> 29/36
- Update 30/40 -> 30/37
- Update 22/32 -> 22/29
- Update 24/34 -> 24/31
- Update 35/45 -> 35/42
- Label changed to: 🥤 + Boisson (+7DH) or 🥤 Ajouter Boisson
- Update Announcement Banner to emphasize: + Boisson +7 DH
"""

import re
import os

MODELS = [
    r'c:\Users\pc\Desktop\menu\menu_model1_emirates.html',
    r'c:\Users\pc\Desktop\menu\menu_model2_urban.html',
    r'c:\Users\pc\Desktop\menu\menu_model3_vibrant.html'
]

PRICE_MAP = {
    39: 36,
    40: 37,
    32: 29,
    34: 31,
    45: 42
}

def update_model(path):
    print("Updating:", os.path.basename(path))
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Labels
    content = content.replace('🥤 MENU COMPLET', '🥤 + BOISSON (+7DH)')
    content = content.replace('🥤 Menu Complet', '🥤 + Boisson (+7DH)')
    content = content.replace('🍟 + SANDWICH', '🍟 SANDWICH + FRITES')
    content = content.replace('🍟 + Sandwich', '🍟 Sandwich + Frites')

    # 2. Update Header Banner
    old_banner_1 = 'TOUS NOS SANDWICHS SONT SERVIS AVEC FRITES CHAUDES !'
    new_banner_1 = '🍟 TOUS NOS SANDWICHS SONT SERVIS AVEC FRITES CHAUDES ! • 🥤 AJOUTER UNE BOISSON : +7 DH'
    if old_banner_1 in content and new_banner_1 not in content:
        content = content.replace(old_banner_1, new_banner_1)

    old_banner_2 = 'Tous nos sandwichs sont servis avec frites chaudes !'
    new_banner_2 = '🍟 Tous nos sandwichs sont servis avec frites chaudes ! • 🥤 Ajouter une Boisson : +7 DH'
    if old_banner_2 in content and new_banner_2 not in content:
        content = content.replace(old_banner_2, new_banner_2)

    # 3. Update Prices for the +Boisson chip
    # Model 1 pattern: <div class="price-col">\s*<span class="label">🥤 \+ BOISSON \(\+7DH\)</span>\s*<span class="num">(\d+)<span class="curr">DH</span></span>
    def repl_m1(m):
        full = m.group(0)
        num = int(m.group(1))
        new_num = PRICE_MAP.get(num, num)
        return full.replace(f'>{num}<', f'>{new_num}<')

    content = re.sub(r'<span class="label">🥤 \+ BOISSON \(\+7DH\)</span>\s*<span class="num">(\d+)<span class="curr">DH</span></span>', repl_m1, content)

    # Model 2 pattern: <div class="price-badge-menu">\s*<span class="p-label">🥤 \+ Boisson \(\+7DH\)</span>\s*<span class="p-val">(\d+)<span>DH</span></span>
    def repl_m2(m):
        full = m.group(0)
        num = int(m.group(1))
        new_num = PRICE_MAP.get(num, num)
        return full.replace(f'>{num}<', f'>{new_num}<')

    content = re.sub(r'<span class="p-label">🥤 \+ Boisson \(\+7DH\)</span>\s*<span class="p-val">(\d+)<span>DH</span></span>', repl_m2, content)

    # Model 3 pattern: <div class="price-chip-menu">\s*<span class="p-tag">🥤 \+ Boisson \(\+7DH\)</span>\s*<span class="p-number">(\d+)<span>DH</span></span>
    def repl_m3(m):
        full = m.group(0)
        num = int(m.group(1))
        new_num = PRICE_MAP.get(num, num)
        return full.replace(f'>{num}<', f'>{new_num}<')

    content = re.sub(r'<span class="p-tag">🥤 \+ Boisson \(\+7DH\)</span>\s*<span class="p-number">(\d+)<span>DH</span></span>', repl_m3, content)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully updated", os.path.basename(path))

for p in MODELS:
    update_model(p)

print("All 3 models updated with +Boisson (+7 DH)!")

