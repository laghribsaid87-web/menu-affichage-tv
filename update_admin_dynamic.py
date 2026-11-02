import json
import os

with open('admin_dynamic.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_tab_btn = '''<button @click="currentTab = 'design'" :class="currentTab === 'design' ? 'bg-red-600 text-white' : 'bg-gray-200 text-gray-700 hover:bg-gray-300'" class="px-4 py-2 font-bold rounded-t-lg transition">
    <i class="fa fa-paint-brush mr-2"></i> Design & Animations
</button>'''

if 'Design & Animations' not in content:
    content = content.replace('<!-- End Tabs -->', new_tab_btn + '\n                <!-- End Tabs -->')

new_tab_content = '''
            <!-- Tab Design -->
            <div v-show="currentTab === 'design'" class="space-y-6">
                <div class="bg-white p-6 rounded-xl shadow border border-gray-200">
                    <h3 class="text-xl font-bold text-gray-800 mb-4"><i class="fa fa-image mr-2 text-red-600"></i> Image Principale (Spotlight)</h3>
                    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                        <div>
                            <label class="block text-gray-700 font-bold mb-2">Position X (Gauche/Droite)</label>
                            <input type="range" min="-200" max="200" v-model.number="config.settings.spotlight_sandwich_x" class="w-full">
                            <div class="text-center font-mono text-sm">{{ config.settings.spotlight_sandwich_x }} px</div>
                        </div>
                        <div>
                            <label class="block text-gray-700 font-bold mb-2">Position Y (Haut/Bas)</label>
                            <input type="range" min="-200" max="200" v-model.number="config.settings.spotlight_sandwich_y" class="w-full">
                            <div class="text-center font-mono text-sm">{{ config.settings.spotlight_sandwich_y }} px</div>
                        </div>
                        <div>
                            <label class="block text-gray-700 font-bold mb-2">Taille (Zoom)</label>
                            <input type="range" min="50" max="200" v-model.number="config.settings.spotlight_sandwich_scale" class="w-full">
                            <div class="text-center font-mono text-sm">{{ config.settings.spotlight_sandwich_scale }} %</div>
                        </div>
                    </div>
                </div>

                <div class="bg-white p-6 rounded-xl shadow border border-gray-200">
                    <h3 class="text-xl font-bold text-gray-800 mb-4"><i class="fa-solid fa-french-fries mr-2 text-yellow-500"></i> Frites (Spotlight)</h3>
                    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                        <div>
                            <label class="block text-gray-700 font-bold mb-2">Position X</label>
                            <input type="range" min="-200" max="200" v-model.number="config.settings.spotlight_fries_x" class="w-full">
                            <div class="text-center font-mono text-sm">{{ config.settings.spotlight_fries_x }} px</div>
                        </div>
                        <div>
                            <label class="block text-gray-700 font-bold mb-2">Position Y</label>
                            <input type="range" min="-200" max="200" v-model.number="config.settings.spotlight_fries_y" class="w-full">
                            <div class="text-center font-mono text-sm">{{ config.settings.spotlight_fries_y }} px</div>
                        </div>
                        <div>
                            <label class="block text-gray-700 font-bold mb-2">Taille (Zoom)</label>
                            <input type="range" min="50" max="200" v-model.number="config.settings.spotlight_fries_scale" class="w-full">
                            <div class="text-center font-mono text-sm">{{ config.settings.spotlight_fries_scale }} %</div>
                        </div>
                    </div>
                </div>

                <div class="bg-white p-6 rounded-xl shadow border border-gray-200">
                    <h3 class="text-xl font-bold text-gray-800 mb-4"><i class="fa fa-magic mr-2 text-purple-600"></i> Animations</h3>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div>
                            <label class="block text-gray-700 font-bold mb-2">Animation Spotlight</label>
                            <select v-model="config.settings.spotlight_anim" class="w-full p-2 border rounded">
                                <option value="pop">Pop 3D (Recommandé)</option>
                                <option value="slide-up">Glisser vers le haut</option>
                                <option value="slide-right">Glisser vers la droite</option>
                                <option value="zoom">Zoom In</option>
                                <option value="fade">Fondu (Fade)</option>
                            </select>
                        </div>
                        <div>
                            <label class="block text-gray-700 font-bold mb-2">Animation Grille (Haut)</label>
                            <select v-model="config.settings.grid_anim" class="w-full p-2 border rounded">
                                <option value="fade">Fondu (Fade)</option>
                                <option value="slide-down">Glisser vers le bas</option>
                                <option value="flip">Retournement (Flip)</option>
                            </select>
                        </div>
                    </div>
                </div>
            </div>
'''

if 'currentTab === \'design\'' not in content:
    content = content.replace('<!-- End Content -->', new_tab_content + '\n            <!-- End Content -->')

with open('admin_dynamic.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated admin_dynamic.html")
