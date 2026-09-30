import re

with open(r'c:\Users\pc\Desktop\menu\dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Navbar
old_nav = """            <div class="flex items-center gap-3">
                <i class="fa-solid fa-paintbrush text-blue-500 text-2xl"></i>
                <h1 class="text-xl font-bold">Menu CMS - WYSIWYG Editor</h1>
            </div>"""
new_nav = """            <div class="flex items-center gap-3">
                <i class="fa-solid fa-paintbrush text-blue-500 text-2xl"></i>
                <h1 class="text-xl font-bold">Menu CMS - WYSIWYG Editor</h1>
                
                <div class="ml-4 flex items-center gap-2 border-l border-slate-700 pl-4">
                    <label class="text-sm text-slate-300">Écran:</label>
                    <select v-model="currentTvId" @change="fetchData" class="bg-slate-800 border border-slate-600 text-white rounded px-2 py-1 outline-none focus:border-blue-500">
                        <option value="1">Télévision 1</option>
                        <option value="2">Télévision 2</option>
                        <option value="3">Télévision 3</option>
                        <option value="4">Télévision 4</option>
                    </select>
                    
                    <button @click="toggleOrientation" class="ml-2 bg-slate-800 hover:bg-slate-700 border border-slate-600 px-3 py-1 rounded text-sm transition flex items-center gap-2" :class="{'border-blue-500 text-blue-400': menuData?.orientation === 'vertical'}">
                        <i class="fa-solid" :class="menuData?.orientation === 'vertical' ? 'fa-mobile-screen' : 'fa-tv'"></i>
                        {{ menuData?.orientation === 'vertical' ? 'Vertical' : 'Horizontal' }}
                    </button>
                    
                    <a :href="'viewer.html?tv=' + currentTvId" target="_blank" class="ml-2 bg-emerald-600 hover:bg-emerald-700 text-white px-3 py-1 rounded text-sm transition flex items-center gap-2">
                        <i class="fa-solid fa-play"></i> Lancer TV
                    </a>
                </div>
            </div>"""
content = content.replace(old_nav, new_nav)

# 2. Vue data
content = content.replace("data() {\n                return {", "data() {\n                return {\n                    currentTvId: '1',")

# 3. fetchData
content = content.replace("const res = await fetch('/api/menu');", "const res = await fetch('/api/menu/' + this.currentTvId);")

# 4. saveData
content = content.replace("const res = await fetch('/api/menu', {", "const res = await fetch('/api/menu/' + this.currentTvId, {")

# 5. toggleOrientation
content = content.replace("methods: {", "methods: {\n                toggleOrientation() {\n                    if(!this.menuData) return;\n                    this.menuData.orientation = this.menuData.orientation === 'vertical' ? 'horizontal' : 'vertical';\n                },")

# 6. mockup-wrapper style
old_wrap = """<div :id="'mockup-wrapper-'+fKey" class="bg-black rounded-lg overflow-hidden relative shadow-2xl border border-slate-700 mockup-wrapper">"""
new_wrap = """<div :id="'mockup-wrapper-'+fKey" class="bg-black rounded-lg overflow-hidden relative shadow-2xl border border-slate-700 mockup-wrapper" :style="menuData.orientation === 'vertical' ? 'width: 273px; height: 486px;' : 'width: 864px; height: 486px;'">"""
content = content.replace(old_wrap, new_wrap)

# 7. tv-mockup style
old_tv = """<div class="tv-mockup absolute top-0 left-0 origin-top-left overflow-hidden" style="width: 1920px; height: 1080px;" :id="'mockup-'+fKey" @contextmenu.prevent="handleContextMenu($event, fKey, null)">"""
new_tv = """<div class="tv-mockup absolute top-0 left-0 origin-top-left overflow-hidden" :style="menuData.orientation === 'vertical' ? 'width: 1080px; height: 1920px; transform: scale(0.2531);' : 'width: 1920px; height: 1080px; transform: scale(0.45);'" :id="'mockup-'+fKey" @contextmenu.prevent="handleContextMenu($event, fKey, null)">"""
content = content.replace(old_tv, new_tv)

with open(r'c:\Users\pc\Desktop\menu\dashboard.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("dashboard.html updated successfully!")
