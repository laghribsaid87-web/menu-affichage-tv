# -*- coding: utf-8 -*-
import os

files = [
    r'c:\Users\pc\Desktop\menu\menu_model1_emirates.html',
    r'c:\Users\pc\Desktop\menu\menu_model2_urban.html',
    r'c:\Users\pc\Desktop\menu\menu_model3_vibrant.html'
]

for p in files:
    with open(p, 'r', encoding='utf-8') as f:
        t = f.read()
    print(os.path.basename(p), ":")
    print("  has applyTransform:", "function applyTransform" in t)
    print("  has studio-floating-bar:", "id=\"studio-floating-bar\"" in t)
    print("  has sbar-duplicate:", "id=\"sbar-duplicate\"" in t)

