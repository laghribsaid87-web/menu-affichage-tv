import sys
sys.stdout.reconfigure(encoding='utf-8')

models = ['menu_model1_emirates.html', 'menu_model2_urban.html', 'menu_model3_vibrant.html']

engine_code = """
    <!-- ========================================== -->
    <!-- 🟢 DYNAMIC PRICING & OFFLINE KIOSK ENGINE -->
    <!-- ========================================== -->
    <script>
    (function() {
        const CACHE_KEY = 'MENU_TV_DYNAMIC_ITEMS';

        function applyLivePrices(data) {
            if (!data || !data.items || !Array.isArray(data.items)) return;
            const cards = document.querySelectorAll('.stall-cell, .urban-card, .pop-card');
            if (!cards.length) return;

            data.items.forEach((item, idx) => {
                const card = cards[idx];
                if (!card) return;

                // 1. Sandwich Price
                const pSandwich = card.querySelector('.price-col:nth-child(1) .num, .price-badge-alone .p-val, .price-chip-alone .p-number');
                if (pSandwich && item.price_sandwich !== undefined) {
                    const currSpan = pSandwich.querySelector('span');
                    const currClass = currSpan && currSpan.className ? currSpan.className : '';
                    pSandwich.innerHTML = `${item.price_sandwich}<span class="${currClass}">DH</span>`;
                }

                // 2. Drink Price (+7 DH)
                const pDrink = card.querySelector('.price-col:nth-child(3) .num, .price-badge-menu .p-val, .price-chip-menu .p-number');
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

        // 1. Immediate offline render from localStorage (0ms!)
        try {
            const cached = localStorage.getItem(CACHE_KEY);
            if (cached) {
                applyLivePrices(JSON.parse(cached));
            }
        } catch(e) {}

        // 2. Background Live Polling & Auto-Sync
        let lastDataHash = "";
        async function syncPrices() {
            try {
                const res = await fetch('/api/menu_items?t=' + Date.now());
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
                // Offline: perfectly normal, localStorage is already active
            }
        }

        // Initial sync + poll every 2.5 seconds
        syncPrices();
        setInterval(syncPrices, 2500);
    })();
    </script>
"""

for m in models:
    path = f"c:/Users/pc/Desktop/menu/{m}"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Remove old engine if present
    if "DYNAMIC PRICING & OFFLINE KIOSK ENGINE" in content:
        start_idx = content.find("<!-- ========================================== -->\n    <!-- 🟢 DYNAMIC PRICING")
        end_idx = content.find("</script>", start_idx) + 9
        content = content[:start_idx] + content[end_idx:]
    
    # Insert before </body>
    if "</body>" in content:
        content = content.replace("</body>", engine_code + "\n</body>")
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Engine installed successfully in {m}")
    else:
        print(f"Error: </body> not found in {m}")

