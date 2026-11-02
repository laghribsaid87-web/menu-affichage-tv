import json
with open('menu_data_smart_1.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
f_key = list(data['formules'].keys())[0]
formule = data['formules'][f_key]
print(f'Formule Name: {formule["name"]}')
print(f'Components count: {len(formule["components"])}')
