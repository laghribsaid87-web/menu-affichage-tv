# -*- coding: utf-8 -*-
import os

FLIP_KEYDOWN = """            } else if (e.key === 'm' || e.key === 'M' || e.key === 'h' || e.key === 'H') {
                const currentFlip = parseInt(activeEl.dataset.flipH || '1', 10);
                activeEl.dataset.flipH = (currentFlip === 1) ? -1 : 1;
                applyTransform(activeEl);
                saveElementState(activeEl);
                positionBar(activeEl);
                e.preventDefault();
                return;"""

files = [
    r'c:\Users\pc\Desktop\menu\menu_model1_emirates.html',
    r'c:\Users\pc\Desktop\menu\menu_model2_urban.html',
    r'c:\Users\pc\Desktop\menu\menu_model3_vibrant.html'
]

for p in files:
    with open(p, 'r', encoding='utf-8') as f:
        t = f.read()
    
    # Check if keydown already has e.key === 'm'
    if "e.key === 'm'" not in t:
        target = "} else if (e.key === 'Escape') {"
        if target in t:
            t = t.replace(target, FLIP_KEYDOWN + "\n            } else if (e.key === 'Escape') {")
            with open(p, 'w', encoding='utf-8') as f:
                f.write(t)
            print("Injected key m into", os.path.basename(p))
        else:
            print("Target escape not found in", os.path.basename(p))
    else:
        print("Key m already in", os.path.basename(p))

