import json
with open('menu_data_smart_1.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
f_key = list(data['formules'].keys())[0]
bg = data['formules'][f_key]['components'][0]
print(f"Width: {bg.get('width')} Color: {bg.get('color')}")
