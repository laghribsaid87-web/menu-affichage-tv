import json
with open('admin_dynamic.html', 'r', encoding='utf-8') as f:
    content = f.read()

settings_html = """
    <!-- Design Settings Section -->
    <div class="mt-8 pt-8 border-t border-gray-300">
        <h2 class="text-3xl font-black text-gray-800 mb-6"><i class="fa fa-paint-brush mr-2 text-red-600"></i> Personnaliser le Design (Smart Theme)</h2>
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
            <div class="bg-white p-6 rounded-xl shadow-lg border border-gray-200">
                <h3 class="text-xl font-bold text-gray-800 mb-4 border-b pb-2">🍔 Sandwich Lkbir (Spotlight)</h3>
                
                <div class="mb-4">
                    <label class="block text-gray-700 font-bold mb-2">Position X (Lissar/Limn)</label>
                    <input type="range" min="-300" max="300" id="set_spotlight_sandwich_x" oninput="updateSetting('spotlight_sandwich_x', this.value)" class="w-full cursor-pointer">
                    <div class="text-center font-mono text-sm font-bold text-blue-600"><span id="val_spotlight_sandwich_x">0</span> px</div>
                </div>
                <div class="mb-4">
                    <label class="block text-gray-700 font-bold mb-2">Position Y (Lfo9/Lta7t)</label>
                    <input type="range" min="-300" max="300" id="set_spotlight_sandwich_y" oninput="updateSetting('spotlight_sandwich_y', this.value)" class="w-full cursor-pointer">
                    <div class="text-center font-mono text-sm font-bold text-blue-600"><span id="val_spotlight_sandwich_y">0</span> px</div>
                </div>
                <div class="mb-4">
                    <label class="block text-gray-700 font-bold mb-2">Taille / Zoom (%)</label>
                    <input type="range" min="50" max="250" id="set_spotlight_sandwich_scale" oninput="updateSetting('spotlight_sandwich_scale', this.value)" class="w-full cursor-pointer">
                    <div class="text-center font-mono text-sm font-bold text-blue-600"><span id="val_spotlight_sandwich_scale">110</span> %</div>
                </div>
                
                <div class="mb-4">
                    <label class="block text-gray-700 font-bold mb-2">Animation Dakhla</label>
                    <select id="set_spotlight_anim" onchange="updateSetting('spotlight_anim', this.value)" class="w-full border-2 border-gray-300 p-2 rounded-lg font-bold">
                        <option value="pop">Pop 3D (Wa3ra)</option>
                        <option value="slide-up">Tle3 men lta7t</option>
                        <option value="slide-right">Dkhel men jnb</option>
                        <option value="zoom">Zoom</option>
                        <option value="fade">Ban bchwia (Fade)</option>
                    </select>
                </div>
            </div>

            <div class="bg-white p-6 rounded-xl shadow-lg border border-gray-200">
                <h3 class="text-xl font-bold text-gray-800 mb-4 border-b pb-2">🍟 Frites (Spotlight)</h3>
                
                <div class="mb-4">
                    <label class="block text-gray-700 font-bold mb-2">Position X (Lissar/Limn)</label>
                    <input type="range" min="-300" max="300" id="set_spotlight_fries_x" oninput="updateSetting('spotlight_fries_x', this.value)" class="w-full cursor-pointer">
                    <div class="text-center font-mono text-sm font-bold text-blue-600"><span id="val_spotlight_fries_x">0</span> px</div>
                </div>
                <div class="mb-4">
                    <label class="block text-gray-700 font-bold mb-2">Position Y (Lfo9/Lta7t)</label>
                    <input type="range" min="-300" max="300" id="set_spotlight_fries_y" oninput="updateSetting('spotlight_fries_y', this.value)" class="w-full cursor-pointer">
                    <div class="text-center font-mono text-sm font-bold text-blue-600"><span id="val_spotlight_fries_y">0</span> px</div>
                </div>
                <div class="mb-4">
                    <label class="block text-gray-700 font-bold mb-2">Taille / Zoom (%)</label>
                    <input type="range" min="50" max="250" id="set_spotlight_fries_scale" oninput="updateSetting('spotlight_fries_scale', this.value)" class="w-full cursor-pointer">
                    <div class="text-center font-mono text-sm font-bold text-blue-600"><span id="val_spotlight_fries_scale">100</span> %</div>
                </div>
            </div>
        </div>
    </div>
"""

if 'Personnaliser le Design' not in content:
    content = content.replace('    </div>\n</div>\n\n<script>', '    </div>\n' + settings_html + '\n</div>\n\n<script>')

js_updates = """
    async function loadData() {
        try {
            const res = await fetch('/api/dynamic_menu');
            menuData = await res.json();
            if(!menuData.bocadillos) menuData.bocadillos = [];
            if(!menuData.sandwiches) menuData.sandwiches = [];
            if(!menuData.settings) menuData.settings = {};
            renderLists();
            loadSettings();
        } catch (e) {
            console.error('Failed to load menu data', e);
        }
    }

    function loadSettings() {
        const s = menuData.settings;
        const keys = ['spotlight_sandwich_x', 'spotlight_sandwich_y', 'spotlight_sandwich_scale', 
                      'spotlight_fries_x', 'spotlight_fries_y', 'spotlight_fries_scale', 'spotlight_anim'];
        keys.forEach(k => {
            if(s[k] !== undefined) {
                const el = document.getElementById('set_' + k);
                if(el) el.value = s[k];
                const valEl = document.getElementById('val_' + k);
                if(valEl) valEl.innerText = s[k];
            }
        });
    }

    function updateSetting(key, value) {
        if(!menuData.settings) menuData.settings = {};
        const numVal = Number(value);
        menuData.settings[key] = isNaN(numVal) ? value : numVal;
        
        const valEl = document.getElementById('val_' + key);
        if(valEl) valEl.innerText = value;
    }
"""

if 'function loadSettings()' not in content:
    content = content.replace('''    async function loadData() {
        try {
            const res = await fetch('/api/dynamic_menu');
            menuData = await res.json();
            if(!menuData.bocadillos) menuData.bocadillos = [];
            if(!menuData.sandwiches) menuData.sandwiches = [];
            renderLists();
        } catch (e) {
            console.error('Failed to load menu data', e);
        }
    }''', js_updates)

with open('admin_dynamic.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated admin_dynamic.html properly!")
