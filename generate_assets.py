import os
import json

base_dir = r'C:\Users\pc\Desktop\menu'
raw_dir = os.path.join(base_dir, 'raw_images')
os.makedirs(raw_dir, exist_ok=True)

svgs = {
    'wood_board.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 250">
        <ellipse cx="400" cy="125" rx="380" ry="110" fill="#5A3B22" />
        <ellipse cx="400" cy="110" rx="380" ry="110" fill="#8B5A2B" />
        <path d="M 400 110 C 200 110, 50 110, 50 110 C 50 150, 200 200, 400 200 C 600 200, 750 150, 750 110 C 750 110, 600 110, 400 110 Z" fill="#A0522D" opacity="0.5" />
        <path d="M 100 110 Q 400 150 700 110" stroke="#5A3B22" stroke-width="4" fill="none" opacity="0.3" />
        <path d="M 150 130 Q 400 170 650 130" stroke="#5A3B22" stroke-width="3" fill="none" opacity="0.2" />
    </svg>''',
    'floor_shadow.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 200">
        <defs>
            <radialGradient id="grad" cx="50%" cy="50%" r="50%" fx="50%" fy="50%">
                <stop offset="0%" stop-color="#000" stop-opacity="0.8" />
                <stop offset="100%" stop-color="#000" stop-opacity="0" />
            </radialGradient>
        </defs>
        <ellipse cx="300" cy="100" rx="280" ry="80" fill="url(#grad)" />
    </svg>''',
    'leaf.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200">
        <path d="M 20 180 Q 50 100 180 20 Q 150 150 20 180" fill="#2E8B57" />
        <path d="M 20 180 Q 100 100 180 20" stroke="#006400" stroke-width="3" fill="none" />
        <path d="M 60 140 Q 100 120 110 80" stroke="#006400" stroke-width="2" fill="none" />
        <path d="M 90 110 Q 140 100 150 60" stroke="#006400" stroke-width="2" fill="none" />
    </svg>'''
}

for filename, content in svgs.items():
    with open(os.path.join(raw_dir, filename), 'w', encoding='utf-8') as f:
        f.write(content)

# Update menu_data_default_1.json if it exists
json_path = os.path.join(base_dir, 'menu_data_default_1.json')
if os.path.exists(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.loads(f.read())
    
    if 'assets' not in data:
        data['assets'] = {}
    if 'decorations' not in data['assets']:
        data['assets']['decorations'] = []
        
    decorations = [
        {'id': 'wood_board', 'name': 'Planche en Bois', 'url': 'raw_images/wood_board.svg'},
        {'id': 'floor_shadow', 'name': 'Ombre (Shadow)', 'url': 'raw_images/floor_shadow.svg'},
        {'id': 'leaf', 'name': 'Feuille (Leaf)', 'url': 'raw_images/leaf.svg'}
    ]
    
    # Add if not exists
    for dec in decorations:
        if not any(d.get('id') == dec['id'] for d in data['assets']['decorations']):
            data['assets']['decorations'].append(dec)
            
    with open(json_path, 'w', encoding='utf-8') as f:
        f.write(json.dumps(data, indent=4))
        
print('Assets created!')
