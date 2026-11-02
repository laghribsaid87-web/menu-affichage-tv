from bs4 import BeautifulSoup

with open("c:/Users/pc/Desktop/menu/menu_model1_emirates.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

cards = soup.select('.stall-cell, .urban-card, .pop-card')
print("Found cards in model 1:", len(cards))

for idx, card in enumerate(cards):
    pSandwich = card.select_one('.price-col:nth-of-type(1) .num, .price-badge-alone .p-val, .price-chip-alone .p-number')
    pDrink = card.select_one('.price-col:nth-of-type(3) .num, .price-badge-menu .p-val, .price-chip-menu .p-number')
    # Or in css :nth-child vs :nth-of-type:
    # In html:
    # <div class="price-col">...</div>
    # <div class="price-sep"></div>
    # <div class="price-col">...</div>
    # The first .price-col is :nth-child(1)
    # The second .price-col is :nth-child(3)!
    p1_child = card.select_one('.price-col:nth-child(1) .num')
    p2_child = card.select_one('.price-col:nth-child(3) .num')
    
    title = card.select_one('.title-3d, .sandwich-name, .pop-title')
    title_text = title.get_text(strip=True) if title else "NO TITLE"
    print(f"Card {idx}: {title_text} | pSandwich={p1_child.get_text(strip=True) if p1_child else 'NONE'} | pDrink={p2_child.get_text(strip=True) if p2_child else 'NONE'}")

