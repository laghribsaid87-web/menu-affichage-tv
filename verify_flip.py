# -*- coding: utf-8 -*-
files = [
    r'c:\Users\pc\Desktop\menu\menu_model1_emirates.html',
    r'c:\Users\pc\Desktop\menu\menu_model2_urban.html',
    r'c:\Users\pc\Desktop\menu\menu_model3_vibrant.html'
]

for p in files:
    with open(p, 'r', encoding='utf-8') as f:
        t = f.read()
    assert 'id="sbar-flip"' in t, f'sbar-flip missing in {p}'
    assert 'flipH' in t, f'flipH missing in {p}'
    assert "e.key === 'm'" in t, f'key m missing in {p}'
    print('Verified OK:', p)

