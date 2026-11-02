import json

with open("c:/Users/pc/Desktop/menu/menu_items.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Screen 3 items
screen3_items = [
    {
        "category": "boisson",
        "desc": "ORANGES DU MAROC PRESSÉES À LA COMMANDE • 100% PUR JUS",
        "id": "jus_orange",
        "img": "processed_images/jus d orange.png",
        "is_available": True,
        "order": 12,
        "price_drink": "0",
        "price_sandwich": "15",
        "screen": 3,
        "title": "D'ORANGE FRAIS",
        "title_prefix": "JUS"
    },
    {
        "category": "boisson",
        "desc": "CANETTE GLACÉE 33CL • COCA-COLA • FANTA • SPRITE • HAWAÏ",
        "id": "soda_canette",
        "img": "processed_images/coca.png",
        "is_available": True,
        "order": 13,
        "price_drink": "0",
        "price_sandwich": "7",
        "screen": 3,
        "title": "CANETTE FRAÎCHE",
        "title_prefix": "SODA"
    },
    {
        "category": "boisson",
        "desc": "CORNET GÉANT • POMMES DE TERRE FRAÎCHES DORÉES ET CROUSTILLANTES",
        "id": "grande_frite",
        "img": "processed_images/fries.png",
        "is_available": True,
        "order": 14,
        "price_drink": "0",
        "price_sandwich": "12",
        "screen": 3,
        "title": "PORTION FRITES",
        "title_prefix": "GRANDE"
    },
    {
        "category": "boisson",
        "desc": "EAU DE SOURCE NATURELLE MAROCAINE • 50CL GLACÉE",
        "id": "eau_minerale",
        "img": "processed_images/drink.png",
        "is_available": True,
        "order": 15,
        "price_drink": "0",
        "price_sandwich": "5",
        "screen": 3,
        "title": "MINÉRALE (50CL)",
        "title_prefix": "EAU"
    }
]

# Check if screen 3 items already exist
existing_ids = [item['id'] for item in data['items']]
for s3 in screen3_items:
    if s3['id'] not in existing_ids:
        data['items'].append(s3)

# Add TV metadata
data['tv_config'] = {
    "1": { "name": "TV 1 (Lissar)", "title": "Menu Bocadillos Chamali", "screen": 1 },
    "2": { "name": "TV 2 (L-Wost)", "title": "Menu Sandwiches Chauds", "screen": 2 },
    "3": { "name": "TV 3 (Limn)", "title": "Menu Boissons & Extras", "screen": 3 }
}

with open("c:/Users/pc/Desktop/menu/menu_items.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("SUCCESS: Added Screen 3 and TV metadata. Total items:", len(data['items']))

