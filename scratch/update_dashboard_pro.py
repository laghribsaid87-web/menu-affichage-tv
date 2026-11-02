import sys

with open("c:/Users/pc/Desktop/menu/dashboard_pro.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add "Envoyer a la TV" button in header
header_target = """<button onclick="saveAllItems()" class="btn-gradient text-white px-4 py-2 md:px-5 md:py-2.5 rounded-xl text-xs md:text-sm font-black flex items-center gap-2 shadow-lg">
                    <i class="fa-solid fa-floppy-disk"></i>
                    <span>Sauvegarder</span>
                </button>"""

header_replace = """<button onclick="saveAllItems()" class="btn-gradient text-white px-3.5 py-2 md:px-4 md:py-2.5 rounded-xl text-xs md:text-sm font-black flex items-center gap-2 shadow-lg">
                    <i class="fa-solid fa-floppy-disk"></i>
                    <span>Sauvegarder</span>
                </button>
                <button onclick="publishToTv()" class="bg-blue-600 hover:bg-blue-700 text-white px-3.5 py-2 md:px-4 md:py-2.5 rounded-xl text-xs md:text-sm font-black flex items-center gap-2 shadow-lg transition">
                    <i class="fa-solid fa-cloud-arrow-up"></i>
                    <span class="hidden sm:inline">Envoyer à la TV</span>
                </button>"""

content = content.replace(header_target, header_replace)

# 2. Add Model Switcher Card
model_card = """        <!-- ACTIVE MODEL SELECTOR -->
        <div class="glass-card rounded-2xl p-4 md:p-5 mb-6 flex flex-col md:flex-row items-stretch md:items-center justify-between gap-4 border border-blue-500/30">
            <div class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-xl bg-blue-500/20 flex items-center justify-center text-blue-400">
                    <i class="fa-solid fa-tv text-lg"></i>
                </div>
                <div>
                    <div class="text-sm font-extrabold text-white">Modèle Actif sur la TV (APK)</div>
                    <div class="text-xs text-gray-400">Sélectionnez le design visuel affiché sur la télévision</div>
                </div>
            </div>
            <div class="flex items-center gap-2">
                <select id="active-model-select" onchange="updateActiveModel(this.value)" class="bg-black/50 border border-white/20 rounded-xl py-2 px-3 text-xs md:text-sm font-bold text-white focus:outline-none focus:border-blue-500 cursor-pointer">
                    <option value="1">👑 Modèle 1 : Luxe Emirates (Bois &amp; Chalkboard)</option>
                    <option value="2">⚡ Modèle 2 : Modern Urban (Orange Électrique)</option>
                    <option value="3">🌊 Modèle 3 : Vibrant Tanger (Bleu Pop)</option>
                </select>
            </div>
        </div>

        <!-- QUICK BOISSON BAR -->"""

content = content.replace("        <!-- QUICK BOISSON BAR -->", model_card)

# 3. Add JS functions
js_add = """        function updateActiveModel(val) {
            if (!menuData.global_settings) menuData.global_settings = {};
            menuData.global_settings.active_model = parseInt(val) || 1;
            showToast("Modèle Modifié", `Le Modèle ${val} est maintenant actif.`);
        }

        async function publishToTv() {
            showToast("Envoi en cours...", "Publication des données vers la TV (Internet)...");
            await saveAllItems();
            try {
                const res = await fetch('/api/publish_to_tv', { method: 'POST' });
                if (res.ok) {
                    showToast("🎉 TV Synchronisée !", "Les nouveaux prix et modèles sont en ligne sur la TV !");
                } else {
                    showToast("Erreur d'envoi", "Vérifiez la connexion Internet.");
                }
            } catch(e) {
                showToast("Erreur Réseau", "Impossible de contacter GitHub.");
            }
        }
"""

content = content.replace("        // Adjust sandwich price with +/-", js_add + "\n        // Adjust sandwich price with +/-")

# Also on loadItems set select
content = content.replace("renderGrid();", """renderGrid();
            if (menuData.global_settings && menuData.global_settings.active_model) {
                const sel = document.getElementById('active-model-select');
                if (sel) sel.value = menuData.global_settings.active_model.toString();
            }""")

with open("c:/Users/pc/Desktop/menu/dashboard_pro.html", "w", encoding="utf-8") as f:
    f.write(content)
print("SUCCESS: Updated dashboard_pro.html")

