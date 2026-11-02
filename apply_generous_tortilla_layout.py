# -*- coding: utf-8 -*-
"""
Apply Tortilla Royale generous proportions across all sandwiches and fries in all 3 models:
1. Fix getElementId to support .pop-card as well as .stall-cell and .urban-card.
2. Update CSS max-width/max-height for generous food sizing.
3. Update JS default scale/pos for sandwiches (1.28) and fries (1.05).
4. Generate complete layout JSON files for Model 1, 2, and 3.
"""

import json
import os
import re

FILES = [
    r'c:\Users\pc\Desktop\menu\menu_model1_emirates.html',
    r'c:\Users\pc\Desktop\menu\menu_model2_urban.html',
    r'c:\Users\pc\Desktop\menu\menu_model3_vibrant.html'
]

# 1. Update HTML and JS in all 3 files
for path in FILES:
    print("Updating file:", os.path.basename(path))
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Fix getElementId to include .pop-card
    content = content.replace(
        "el.closest('.stall-cell, .urban-card, .vibrant-card')",
        "el.closest('.stall-cell, .urban-card, .vibrant-card, .pop-card')"
    )

    # Increase max-width & max-height in CSS for .food-sandwich
    content = re.sub(
        r'(\.food-sandwich\s*\{[^}]*max-width:\s*)\d+px;',
        r'\g<1>480px;',
        content
    )
    content = re.sub(
        r'(\.food-sandwich\s*\{[^}]*max-height:\s*)\d+px;',
        r'\g<1>230px;',
        content
    )

    # Update default values in applyAllLayout
    old_default = """                } else {
                    el.dataset.scale = 1;
                    el.dataset.tx = 0;
                    el.dataset.ty = 0;
                    el.dataset.rot = isFries(el) ? 6 : 0;
                    el.dataset.flipH = 1;
                    el.dataset.zIndex = isFries(el) ? 4 : (isSandwich(el) ? 10 : 20);
                }"""

    new_default = """                } else {
                    el.dataset.scale = isSandwich(el) ? 1.28 : (isFries(el) ? 1.05 : 1);
                    el.dataset.tx = isSandwich(el) ? -22 : (isFries(el) ? 12 : 0);
                    el.dataset.ty = isSandwich(el) ? 8 : (isFries(el) ? -6 : 0);
                    el.dataset.rot = isFries(el) ? 6 : 0;
                    el.dataset.flipH = 1;
                    el.dataset.zIndex = isFries(el) ? 4 : (isSandwich(el) ? 10 : 20);
                }"""

    if old_default in content:
        content = content.replace(old_default, new_default)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated HTML & JS files successfully!")

# 2. Build full layout dictionary for 6 cards on screen-1, and 5 cards on screen-2
full_layout = {}

# Screen 1: Bocadillos (6 cells)
for c in range(6):
    full_layout[f"screen-1_c{c}_sandwich"] = {
        "scale": 1.28,
        "x": -22,
        "y": 8,
        "rot": 0,
        "zIndex": 10,
        "flipH": 1
    }
    full_layout[f"screen-1_c{c}_frites"] = {
        "scale": 1.05,
        "x": 14,
        "y": -6,
        "rot": 6,
        "zIndex": 4,
        "flipH": 1
    }

# Screen 2: Sandwiches Chauds (5 cells)
for c in range(5):
    full_layout[f"screen-2_c{c}_sandwich"] = {
        "scale": 1.28,
        "x": -22,
        "y": 8,
        "rot": 0,
        "zIndex": 10,
        "flipH": 1
    }
    full_layout[f"screen-2_c{c}_frites"] = {
        "scale": 1.05,
        "x": 14,
        "y": -6,
        "rot": 6,
        "zIndex": 4,
        "flipH": 1
    }

# Save layout JSON for all 3 models
json_files = [
    r'c:\Users\pc\Desktop\menu\layout_menu_model1_emirates.json',
    r'c:\Users\pc\Desktop\menu\layout_menu_model2_urban.json',
    r'c:\Users\pc\Desktop\menu\layout_menu_model3_vibrant.json'
]

for jf in json_files:
    with open(jf, 'w', encoding='utf-8') as f:
        json.dump(full_layout, f, indent=2)
    print("Saved generous layout to:", os.path.basename(jf))

print("All models now use Tortilla Royale generous proportions across ALL sandwiches and fries!")

