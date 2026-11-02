import sys

with open("c:/Users/pc/Desktop/menu/dashboard_pro.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update onchange to oninput
content = content.replace(
    'onchange="updateSandwichPrice(${index}, this.value)"',
    'oninput="updateSandwichPrice(${index}, this.value)"'
)
content = content.replace(
    'onchange="updateDrinkPrice(${index}, this.value)"',
    'oninput="updateDrinkPrice(${index}, this.value)"'
)

# 2. Add API_BASE and BroadcastChannel
api_base_code = """        const API_BASE = (window.location.protocol === 'file:') ? 'http://localhost:8000' : '';
        let menuData = { items: [], global_settings: {}, tv_config: {} };"""

content = content.replace(
    "let menuData = { items: [], global_settings: {}, tv_config: {} };",
    api_base_code
)

# 3. Replace loadItems with API_BASE
old_load = """        async function loadItems() {
            try {
                const res = await fetch('/api/menu_items?t=' + Date.now());"""

new_load = """        async function loadItems() {
            try {
                let res = await fetch(API_BASE + '/api/menu_items?t=' + Date.now());
                if (!res.ok) {
                    res = await fetch(API_BASE + '/menu_items.json?t=' + Date.now());
                }"""

content = content.replace(old_load, new_load)

# 4. Replace saveAllItems with BroadcastChannel & error handling
old_save = """        async function saveAllItems() {
            try {
                localStorage.setItem('MENU_ITEMS_CACHE', JSON.stringify(menuData));
                const res = await fetch('/api/menu_items', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(menuData)
                });
                if (res.ok) {
                    showToast("Prix Enregistrés !", "Les télévisions ont reçu les nouveaux prix.");
                } else {
                    showToast("Enregistré Localement", "Stocké en mémoire locale.");
                }
            } catch(e) {
                showToast("Enregistré Localement", "Mode hors-ligne.");
            }
        }"""

new_save = """        async function saveAllItems() {
            try {
                // 1. Instant LocalStorage & Cross-Tab Broadcast (0ms)
                localStorage.setItem('MENU_ITEMS_CACHE', JSON.stringify(menuData));
                if (window.BroadcastChannel) {
                    const bc = new BroadcastChannel('MENU_TV_CHANNEL');
                    bc.postMessage({ type: 'PRICES_UPDATED', data: menuData });
                }

                // 2. Persist to Backend Server
                const res = await fetch(API_BASE + '/api/menu_items', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(menuData)
                });

                if (res.ok) {
                    showToast("✅ Prix Enregistrés !", "Les télévisions ont reçu les nouveaux prix en direct.");
                } else {
                    showToast("⚠️ Attention", "Enregistré dans le navigateur mais serveur injoignable.");
                }
            } catch(e) {
                console.error("Save error:", e);
                showToast("💾 Enregistré Localement", "Mode hors-ligne (Vérifiez si Localhost est lancé).");
            }
        }"""

content = content.replace(old_save, new_save)

# 5. Replace publishToTv
old_publish = """        async function publishToTv() {
            showToast("Publication TV...", "Synchronisation avec GitHub Pages...");
            await saveAllItems();
            try {
                const res = await fetch('/api/publish_to_tv', { method: 'POST' });"""

new_publish = """        async function publishToTv() {
            showToast("Publication TV...", "Synchronisation avec GitHub Pages...");
            await saveAllItems();
            try {
                const res = await fetch(API_BASE + '/api/publish_to_tv', { method: 'POST' });"""

content = content.replace(old_publish, new_publish)

with open("c:/Users/pc/Desktop/menu/dashboard_pro.html", "w", encoding="utf-8") as f:
    f.write(content)

print("SUCCESS: Updated dashboard_pro.html with oninput, API_BASE and BroadcastChannel.")

