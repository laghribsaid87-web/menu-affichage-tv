# -*- coding: utf-8 -*-
with open(r'c:\Users\pc\Desktop\menu\menu_model4_behance.html', 'r', encoding='utf-8') as f:
    text = f.read()

drink_css = """
        /* Side Cold Drink */
        .hero-drink-img {
            position: absolute;
            bottom: 40px;
            left: 20px;
            width: 140px;
            height: auto;
            z-index: 9;
            filter: drop-shadow(0 15px 25px rgba(0,0,0,0.95));
            animation: hero-drink-float 5s ease-in-out infinite alternate;
        }
        @keyframes hero-drink-float {
            0% { transform: translateY(0px) rotate(2deg); }
            100% { transform: translateY(-7px) rotate(-1deg); }
        }
"""

if '.hero-drink-img' not in text:
    text = text.replace('/* Side Fry Cone */', drink_css + '\n        /* Side Fry Cone */')

old_part = '<!-- Hero Sandwich -->'
new_part = """<!-- Cold Drink -->
                    <img src="/processed_images/coca.png" 
                         class="hero-drink-img editable-item" 
                         id="hero_drink" 
                         data-item-id="hero_drink" 
                         alt="Boisson Fraîche">

                    <!-- Hero Sandwich -->"""

if 'hero_drink' not in text and old_part in text:
    text = text.replace(old_part, new_part)

with open(r'c:\Users\pc\Desktop\menu\menu_model4_behance.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('Drink added successfully!')

