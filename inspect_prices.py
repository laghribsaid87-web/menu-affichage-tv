# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
with open(r'c:\Users\pc\Desktop\menu\menu_model3_vibrant.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'<div class="price-chip-menu">.*?</div>', text, re.DOTALL)
if m:
    print("Model 3 price-chip-menu sample:")
    print(m.group(0))
