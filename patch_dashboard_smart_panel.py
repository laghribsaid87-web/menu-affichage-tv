import os

dash_path = r'c:\Users\pc\Desktop\menu\dashboard.html'
with open(dash_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Define the smart helper methods to insert into Vue methods
methods_to_add = '''
                // Emirates Smart Helpers for Price, Title and Ribbon
                isEmiratesPrice(comp) {
                    return comp && comp.type === 'customText' && typeof comp.content === 'string' && (comp.content.includes('#fcd535') || comp.content.includes('SEUL'));
                },
                getPriceSeul(comp) {
                    if (!comp || !comp.content) return '';
                    const m = comp.content.match(/SEUL[\\s\\S]*?>(\\+?\\d+)<span/i);
                    return m ? m[1] : '';
                },
                setPriceSeul(comp, val) {
                    if (!comp || !comp.content) return;
                    comp.content = comp.content.replace(/(SEUL[\\s\\S]*?>)(\\+?\\d+)(<span)/i, `$1${val}$3`);
                },
                getPriceMenu(comp) {
                    if (!comp || !comp.content) return '';
                    const m = comp.content.match(/MENU[\\s\\S]*?>(\\d+)<span/i);
                    return m ? m[1] : '';
                },
                setPriceMenu(comp, val) {
                    if (!comp || !comp.content) return;
                    comp.content = comp.content.replace(/(MENU[\\s\\S]*?>)(\\d+)(<span)/i, `$1${val}$3`);
                },
                isEmiratesTitle(comp) {
                    return comp && comp.type === 'customText' && typeof comp.content === 'string' && comp.content.includes('font-size:42px');
                },
                getTitleText(comp) {
                    if (!comp || !comp.content) return '';
                    const m = comp.content.match(/font-size:42px[\\s\\S]*?>([^<]+)<\\/span>/i);
                    return m ? m[1].trim() : '';
                },
                setTitleText(comp, val) {
                    if (!comp || !comp.content) return;
                    comp.content = comp.content.replace(/(font-size:42px[\\s\\S]*?>)([^<]+)(<\\/span>)/i, `$1${val}$3`);
                },
                isEmiratesRibbon(comp) {
                    return comp && comp.type === 'customText' && typeof comp.content === 'string' && comp.content.includes('white-space:nowrap');
                },
                getRibbonText(comp) {
                    if (!comp || !comp.content) return '';
                    const m = comp.content.match(/white-space:nowrap;[^>]*>\\s*([\\s\\S]*?)\\s*<\\/div>/i);
                    return m ? m[1].trim() : '';
                },
                setRibbonText(comp, val) {
                    if (!comp || !comp.content) return;
                    comp.content = comp.content.replace(/(white-space:nowrap;[^>]*>\\s*)([\\s\\S]*?)(\\s*<\\/div>)/i, `$1${val}$3`);
                },
'''

# 2. Smart UI Template to replace the plain textarea
old_editor = '''                                                <div class="mb-2">
                                                    <label
                                                        class="text-[10px] text-slate-500 uppercase block mb-1">Contenu
                                                        du Texte</label>
                                                    <textarea v-model="comp.content" rows="2"
                                                        class="w-full bg-white shadow-sm border border-gray-200 rounded px-2 py-1 text-sm text-slate-800 outline-none focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 transition-shadow"></textarea>
                                                </div>'''

new_editor = '''                                                <!-- Smart Emirates Price Editor -->
                                                <div v-if="isEmiratesPrice(comp)" class="mb-3 p-3 bg-amber-50 rounded-lg border-2 border-amber-300 shadow-sm">
                                                    <div class="text-xs font-black text-amber-900 uppercase mb-2 flex items-center gap-1">
                                                        <i class="fa fa-tag text-amber-600"></i> Modifier le Prix Directement :
                                                    </div>
                                                    <div class="grid grid-cols-2 gap-3">
                                                        <div>
                                                            <label class="text-[10px] font-black text-slate-600 block mb-1">PRIX SEUL (DH)</label>
                                                            <div class="flex items-center">
                                                                <input type="text" :value="getPriceSeul(comp)" @input="setPriceSeul(comp, $event.target.value)"
                                                                    class="w-full bg-white font-black text-xl text-center text-slate-900 border-2 border-amber-400 rounded-l py-1 outline-none focus:ring-2 focus:ring-amber-500">
                                                                <span class="bg-amber-400 text-amber-950 font-black px-2 py-2 text-xs rounded-r">DH</span>
                                                            </div>
                                                        </div>
                                                        <div>
                                                            <label class="text-[10px] font-black text-slate-600 block mb-1">PRIX MENU (DH)</label>
                                                            <div class="flex items-center">
                                                                <input type="text" :value="getPriceMenu(comp)" @input="setPriceMenu(comp, $event.target.value)"
                                                                    class="w-full bg-white font-black text-xl text-center text-slate-900 border-2 border-amber-400 rounded-l py-1 outline-none focus:ring-2 focus:ring-amber-500">
                                                                <span class="bg-amber-400 text-amber-950 font-black px-2 py-2 text-xs rounded-r">DH</span>
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <div class="text-[10px] text-amber-700 mt-2 font-medium text-center">Tapez le prix ici, le design et le cadre s\'actualisent automatiquement !</div>
                                                </div>

                                                <!-- Smart Emirates Title Editor -->
                                                <div v-else-if="isEmiratesTitle(comp)" class="mb-3 p-3 bg-red-50 rounded-lg border-2 border-red-300 shadow-sm">
                                                    <label class="text-xs font-black text-red-900 uppercase mb-1 block">
                                                        <i class="fa fa-burger text-red-600"></i> Nom du Sandwich (Titre 3D) :
                                                    </label>
                                                    <input type="text" :value="getTitleText(comp)" @input="setTitleText(comp, $event.target.value)"
                                                        class="w-full bg-white font-black text-lg text-slate-900 border-2 border-red-400 rounded px-3 py-1.5 outline-none focus:ring-2 focus:ring-red-500">
                                                </div>

                                                <!-- Smart Emirates Ribbon Editor -->
                                                <div v-else-if="isEmiratesRibbon(comp)" class="mb-3 p-3 bg-slate-100 rounded-lg border-2 border-slate-300 shadow-sm">
                                                    <label class="text-xs font-black text-slate-800 uppercase mb-1 block">
                                                        <i class="fa fa-list text-amber-500"></i> Ingrédients du Ruban :
                                                    </label>
                                                    <textarea :value="getRibbonText(comp)" @input="setRibbonText(comp, $event.target.value)" rows="2"
                                                        class="w-full bg-white font-bold text-xs text-slate-900 border-2 border-slate-400 rounded px-2 py-1 outline-none focus:ring-2 focus:ring-slate-500"></textarea>
                                                </div>

                                                <!-- Generic or Raw Code Accordion -->
                                                <details class="mb-2 text-xs text-slate-400" :open="!isEmiratesPrice(comp) && !isEmiratesTitle(comp) && !isEmiratesRibbon(comp)">
                                                    <summary class="cursor-pointer hover:text-slate-600 font-semibold mb-1">
                                                        {{ (isEmiratesPrice(comp) || isEmiratesTitle(comp) || isEmiratesRibbon(comp)) ? '⚙️ Voir / Modifier le Code HTML brut' : 'Contenu du Texte' }}
                                                    </summary>
                                                    <textarea v-model="comp.content" rows="2"
                                                        class="w-full bg-slate-50 shadow-inner border border-gray-300 rounded px-2 py-1 text-xs font-mono text-slate-700 outline-none focus:border-indigo-500"></textarea>
                                                </details>'''

# Apply insertions
if old_editor in content:
    content = content.replace(old_editor, new_editor)
    print("Editor UI replaced successfully!")
else:
    print("WARNING: old_editor not found exactly, attempting normalized search...")
    # normalize whitespace
    import re
    p = re.compile(r'<div class="mb-2">\s*<label[^>]*>Contenu\s*du Texte</label>\s*<textarea v-model="comp\.content"[^>]*></textarea>\s*</div>')
    if p.search(content):
        content = p.sub(new_editor, content)
        print("Editor UI replaced via regex!")
    else:
        print("Failed to replace Editor UI!")

# Insert methods
target_method_anchor = 'methods: {'
if target_method_anchor in content and 'isEmiratesPrice' not in content:
    content = content.replace(target_method_anchor, target_method_anchor + '\n' + methods_to_add)
    print("Methods added successfully!")
else:
    print("Methods already added or anchor not found.")

with open(dash_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("dashboard.html updated successfully!")

