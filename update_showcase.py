# -*- coding: utf-8 -*-
with open(r'c:\Users\pc\Desktop\menu\menu_showcase.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Replace tabs
target_tabs = '''        <div class="tabs-container">
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

# Let's find '<div class="tabs-container">' up to '</div>'
start_idx = text.find('<div class="tabs-container">')
end_idx = text.find('</div>', start_idx) + 6

new_tabs = '''<div class="tabs-container">
            <button class="tab-btn active-2" id="tab-4" onclick="switchModel(4)" style="background: linear-gradient(135deg, #ff6b00 0%, #dc2626 100%); color:#ffffff; border-color:#f59e0b; box-shadow: 0 4px 20px rgba(255,107,0,0.5);">
                🔥 Modèle 4 : Behance Fast-Food Pro (Ardoise &amp; Tacos Gratiné)
            </button>
            <button class="tab-btn" id="tab-1" onclick="switchModel(1)">
                👑 Modèle 1 : Luxe Emirates (Bois)
            </button>
            <button class="tab-btn" id="tab-2" onclick="switchModel(2)">
                ⚡ Modèle 2 : Modern Urban (Orange)
            </button>
            <button class="tab-btn" id="tab-3" onclick="switchModel(3)">
                🌊 Modèle 3 : Vibrant Tanger (Bleu)
            </button>
        </div>'''

if start_idx != -1 and end_idx != -1:
    text = text[:start_idx] + new_tabs + text[end_idx:]

# Update models object in script
old_models = '''        const models = {
            1: { url: '/menu_model1_emirates.html', class: 'active-1' },
            2: { url: '/menu_model2_urban.html', class: 'active-2' },
            3: { url: '/menu_model3_vibrant.html', class: 'active-3' }
        };'''

new_models = '''        const models = {
            1: { url: '/menu_model1_emirates.html', class: 'active-1' },
            2: { url: '/menu_model2_urban.html', class: 'active-2' },
            3: { url: '/menu_model3_vibrant.html', class: 'active-3' },
            4: { url: '/menu_model4_behance.html', class: 'active-2' }
        };'''

text = text.replace(old_models, new_models)
text = text.replace('[1, 2, 3].forEach', '[1, 2, 3, 4].forEach')
text = text.replace("if (e.key === '3') switchModel(3);", "if (e.key === '3') switchModel(3);\n            if (e.key === '4') switchModel(4);")

# Default frame to model 4
text = text.replace('src="/menu_model1_emirates.html"', 'src="/menu_model4_behance.html"')
text = text.replace('href="/menu_model1_emirates.html"', 'href="/menu_model4_behance.html"')

with open(r'c:\Users\pc\Desktop\menu\menu_showcase.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated showcase with Model 4!')

