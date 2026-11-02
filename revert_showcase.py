# -*- coding: utf-8 -*-
with open(r'c:\Users\pc\Desktop\menu\menu_showcase.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

clean_tabs = '''<div class="tabs-container">
            <button class="tab-btn active-1" id="tab-1" onclick="switchModel(1)">
                👑 Modèle 1 : Luxe Emirates (Bois &amp; Chalkboard)
            </button>
            <button class="tab-btn" id="tab-2" onclick="switchModel(2)">
                ⚡ Modèle 2 : Modern Urban 2026 (Orange Électrique)
            </button>
            <button class="tab-btn" id="tab-3" onclick="switchModel(3)">
                🌊 Modèle 3 : Vibrant Tanger (Bleu &amp; Pop)
            </button>
        </div>'''

text = re.sub(r'<div class="tabs-container">.*?</div>', clean_tabs, text, flags=re.DOTALL)

clean_models = '''        const models = {
            1: { url: '/menu_model1_emirates.html', class: 'active-1' },
            2: { url: '/menu_model2_urban.html', class: 'active-2' },
            3: { url: '/menu_model3_vibrant.html', class: 'active-3' }
        };'''

text = re.sub(r'const models = \{.*?\};', clean_models, text, flags=re.DOTALL)
text = text.replace('[1, 2, 3, 4].forEach', '[1, 2, 3].forEach')
text = text.replace("if (e.key === '4') switchModel(4);", "")
text = text.replace('src="/menu_model4_behance.html"', 'src="/menu_model1_emirates.html"')
text = text.replace('href="/menu_model4_behance.html"', 'href="/menu_model1_emirates.html"')

with open(r'c:\Users\pc\Desktop\menu\menu_showcase.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('Reverted cleanly!')

