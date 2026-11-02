import sys
import re

models = ['menu_model1_emirates.html', 'menu_model2_urban.html', 'menu_model3_vibrant.html']

item_ids = [
    'complet', 'tortilla_royale', 'thon', 'tortilla', 'tangerois', 'cheese',
    'americain', 'viande_hachee', 'mixte', 'poulet', 'saucisse'
]

engine_code = """
    <!-- ========================================== -->
    <!-- 🟢 DYNAMIC PRICING & OFFLINE KIOSK ENGINE  -->
    <!-- ========================================== -->
    <script>
    (function() {
        const CACHE_KEY = 'MENU_TV_DYNAMIC_ITEMS';

        function applyLivePrices(data) {
            if (!data || !data.items || !Array.isArray(data.items)) return;

            data.items.forEach(item => {
                // Find card by data-item-id
                const card = document.querySelector(`[data-item-id="${item.id}"]`);
                if (!card) return;

                // 1. Sandwich Price (first price)
                const pSandwich = card.querySelector('.price-col:nth-of-type(1) .num, .price-badge-alone .p-val, .price-chip-alone .p-number, .num, .p-val, .p-number');
                if (pSandwich && item.price_sandwich !== undefined) {
                    const currSpan = pSandwich.querySelector('span');
                    const currClass = currSpan && currSpan.className ? currSpan.className : '';
                    pSandwich.innerHTML = `${item.price_sandwich}<span class="${currClass}">DH</span>`;
                }

                // 2. Drink Price (second price)
                const pDrink = card.querySelector('.price-col:nth-of-type(3) .num, .price-col:last-child .num, .price-badge-menu .p-val, .price-chip-menu .p-number');
                if (pDrink && item.price_drink !== undefined) {
                    const currSpan = pDrink.querySelector('span');
                    const currClass = currSpan && currSpan.className ? currSpan.className : '';
                    const dVal = item.price_drink.toString().startsWith('+') ? item.price_drink : ('+' + item.price_drink);
                    pDrink.innerHTML = `${dVal}<span class="${currClass}">DH</span>`;
                }

                // 3. Stock Availability
                if (item.is_available === false) {
                    card.style.opacity = '0.35';
                    card.style.filter = 'grayscale(0.85)';
                } else {
                    card.style.opacity = '1';
                    card.style.filter = 'none';
                }
            });
        }

        // 1. Instant offline render from localStorage (0ms!)
        try {
            const cached = localStorage.getItem(CACHE_KEY);
            if (cached) {
                applyLivePrices(JSON.parse(cached));
            }
        } catch(e) {}

        // 2. Instant Cross-Tab Broadcast Channel (0ms sync when saved in dashboard!)
        if (window.BroadcastChannel) {
            const bc = new BroadcastChannel('MENU_TV_CHANNEL');
            bc.onmessage = (event) => {
                if (event.data && event.data.type === 'PRICES_UPDATED' && event.data.data) {
                    applyLivePrices(event.data.data);
                }
            };
        }

        // 3. Background Polling & Auto-Sync (Fallback to static JSON if API 404s)
        let lastDataHash = "";
        async function syncPrices() {
            try {
                let res = await fetch('/api/menu_items?t=' + Date.now());
                if (!res.ok) {
                    res = await fetch('menu_items.json?t=' + Date.now());
                }
                if (res.ok) {
                    const text = await res.text();
                    if (text !== lastDataHash) {
                        lastDataHash = text;
                        localStorage.setItem(CACHE_KEY, text);
                        const data = JSON.parse(text);
                        applyLivePrices(data);
                    }
                }
            } catch(e) {
                // Offline fallback
            }
        }

        syncPrices();
        setInterval(syncPrices, 2000);
    })();
    </script>
"""

for m in models:
    path = f"c:/Users/pc/Desktop/menu/{m}"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Tag each of the 11 cards with data-item-id
    # Find card tags
    card_classes = ['stall-cell', 'urban-card', 'pop-card']
    for cls in card_classes:
        pattern = rf'(class=["\'][^"\']*\b{cls}\b[^"\']*["\'])'
        matches = list(re.finditer(pattern, content))
        if matches and len(matches) >= 11:
            # Replace each from last to first
            for i in range(10, -1, -1):
                match = matches[i]
                start, end = match.span()
                matched_str = match.group(0)
                # Avoid duplicate data-item-id
                if f'data-item-id="{item_ids[i]}"' not in content[max(0, start-40):end+40]:
                    new_str = f'{matched_str} data-item-id="{item_ids[i]}"'
                    content = content[:start] + new_str + content[end:]
            print(f"Tagged 11 cards with data-item-id in {m}")
            break

    # 2. Replace the dynamic price engine
    if "DYNAMIC PRICING & OFFLINE KIOSK ENGINE" in content:
        start_idx = content.find("<!-- ========================================== -->\n    <!-- 🟢 DYNAMIC PRICING")
        end_idx = content.find("</script>", start_idx) + 9
        content = content[:start_idx] + content[end_idx:]

    content = content.replace("</body>", engine_code + "\n</body>")

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Updated live pricing engine in {m}")

