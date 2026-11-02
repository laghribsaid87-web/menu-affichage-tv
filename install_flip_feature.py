# -*- coding: utf-8 -*-
"""
Install Horizontal Flip (Miroir Droite / Gauche) feature across:
- menu_model1_emirates.html
- menu_model2_urban.html
- menu_model3_vibrant.html
"""

import re
import os

FLIP_CSS = """
        .studio-pill-btn.btn-flip {
            border-color: #06b6d4;
            color: #67e8f9;
        }
        .studio-pill-btn.btn-flip:hover {
            background: #06b6d4;
            color: #111;
            transform: scale(1.05);
        }
"""

FLIP_BUTTON_HTML = """        <!-- Miroir Horizontal (Droite / Gauche) Button -->
        <button class="studio-pill-btn btn-flip" id="sbar-flip" title="Retourner horizontalement (Miroir Droite / Gauche)">🔄 Miroir (↔️)</button>
"""

def update_file(path):
    print("Patching:", os.path.basename(path))
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add CSS for .studio-pill-btn.btn-flip if not present
    if '.studio-pill-btn.btn-flip' not in content:
        content = content.replace('.studio-pill-btn.btn-dup {', FLIP_CSS + '\n        .studio-pill-btn.btn-dup {')

    # 2. Add Button HTML into #studio-floating-bar if not present
    if 'id="sbar-flip"' not in content:
        content = content.replace('<!-- Dupliquer Button -->', FLIP_BUTTON_HTML + '\n        <!-- Dupliquer Button -->')

    # 3. Update applyTransform
    old_apply = """            const transformVal = `translateX(${baseShift + tx}px) translateY(${ty}px) scale(${s}) rotate(${r}deg)`;"""
    new_apply = """            const flipH = parseInt(el.dataset.flipH || '1', 10);
            const transformVal = `translateX(${baseShift + tx}px) translateY(${ty}px) scale(${s * flipH}, ${s}) rotate(${r * flipH}deg)`;"""
    if old_apply in content:
        content = content.replace(old_apply, new_apply)
    elif 'const flipH = parseInt' not in content:
        print("Warning: old_apply pattern not found directly, checking regex")
        content = re.sub(
            r'const transformVal = `translateX\(\$\{baseShift \+ tx\}px\) translateY\(\$\{ty\}px\) scale\(\$\{s\}\) rotate\(\$\{r\}deg\)`;',
            new_apply,
            content
        )

    # 4. Update applyAllLayout to load flipH
    old_layout_load = """                    el.dataset.rot = layoutState[id].rot ?? (isFries(el) ? 6 : 0);"""
    new_layout_load = """                    el.dataset.rot = layoutState[id].rot ?? (isFries(el) ? 6 : 0);
                    el.dataset.flipH = layoutState[id].flipH ?? 1;"""
    if old_layout_load in content and 'el.dataset.flipH = layoutState[id].flipH' not in content:
        content = content.replace(old_layout_load, new_layout_load)

    old_layout_default = """                    el.dataset.rot = isFries(el) ? 6 : 0;
                    el.dataset.zIndex = isFries(el) ? 4 : (isSandwich(el) ? 10 : 20);"""
    new_layout_default = """                    el.dataset.rot = isFries(el) ? 6 : 0;
                    el.dataset.flipH = 1;
                    el.dataset.zIndex = isFries(el) ? 4 : (isSandwich(el) ? 10 : 20);"""
    if old_layout_default in content and 'el.dataset.flipH = 1;' not in content:
        content = content.replace(old_layout_default, new_layout_default)

    # 5. Update saveElementState to persist flipH
    old_save = """            layoutState[id].rot = parseFloat(el.dataset.rot || (isFries(el) ? 6 : 0));"""
    new_save = """            layoutState[id].rot = parseFloat(el.dataset.rot || (isFries(el) ? 6 : 0));
            layoutState[id].flipH = parseInt(el.dataset.flipH || '1', 10);"""
    if old_save in content and 'layoutState[id].flipH' not in content:
        content = content.replace(old_save, new_save)

    # 6. Update createCloneElement to carry over flipH
    old_clone_saved = """                clone.dataset.rot = savedProps.rot;"""
    new_clone_saved = """                clone.dataset.rot = savedProps.rot;
                clone.dataset.flipH = savedProps.flipH || 1;"""
    if old_clone_saved in content and 'clone.dataset.flipH = savedProps.flipH' not in content:
        content = content.replace(old_clone_saved, new_clone_saved)

    old_clone_orig = """                clone.dataset.rot = origEl.dataset.rot || (isFries(origEl) ? 6 : 0);"""
    new_clone_orig = """                clone.dataset.rot = origEl.dataset.rot || (isFries(origEl) ? 6 : 0);
                clone.dataset.flipH = origEl.dataset.flipH || 1;"""
    if old_clone_orig in content and 'clone.dataset.flipH = origEl.dataset.flipH' not in content:
        content = content.replace(old_clone_orig, new_clone_orig)

    # 7. Add flip button click listener and keyboard shortcut
    flip_listener_code = """
        // MIROIR HORIZONTAL (Flip Droite / Gauche)
        const flipBtn = document.getElementById('sbar-flip');
        if (flipBtn) {
            flipBtn.addEventListener('click', (e) => {
                e.stopPropagation();
                if (!activeEl) return;
                const currentFlip = parseInt(activeEl.dataset.flipH || '1', 10);
                activeEl.dataset.flipH = (currentFlip === 1) ? -1 : 1;
                applyTransform(activeEl);
                saveElementState(activeEl);
                positionBar(activeEl);
            });
        }
"""
    if 'id="sbar-flip"' in content and 'sbar-flip' not in content.split('// DUPLIQUER')[0] if '// DUPLIQUER' in content else True:
        if '// MIROIR HORIZONTAL' not in content:
            content = content.replace('// DUPLIQUER (Clone Element)', flip_listener_code + '\n        // DUPLIQUER (Clone Element)')

    # Add keyboard shortcut 'm' or 'h'
    old_key_rot = """            else if (e.key === 'r' || e.key === 'R') {
                const step = e.shiftKey ? -5 : 5;
                el.dataset.rot = (parseFloat(el.dataset.rot || (isFries(el) ? 6 : 0)) + step);
                applyTransform(el);
                saveElementState(el);
                positionBar(el);
                e.preventDefault();
            }"""
    new_key_rot = """            else if (e.key === 'r' || e.key === 'R') {
                const step = e.shiftKey ? -5 : 5;
                el.dataset.rot = (parseFloat(el.dataset.rot || (isFries(el) ? 6 : 0)) + step);
                applyTransform(el);
                saveElementState(el);
                positionBar(el);
                e.preventDefault();
            }
            else if (e.key === 'm' || e.key === 'M' || e.key === 'h' || e.key === 'H') {
                const currentFlip = parseInt(el.dataset.flipH || '1', 10);
                el.dataset.flipH = (currentFlip === 1) ? -1 : 1;
                applyTransform(el);
                saveElementState(el);
                positionBar(el);
                e.preventDefault();
            }"""
    if old_key_rot in content and "e.key === 'm'" not in content:
        content = content.replace(old_key_rot, new_key_rot)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Done:", os.path.basename(path))

files = [
    r'c:\Users\pc\Desktop\menu\menu_model1_emirates.html',
    r'c:\Users\pc\Desktop\menu\menu_model2_urban.html',
    r'c:\Users\pc\Desktop\menu\menu_model3_vibrant.html'
]

for p in files:
    update_file(p)

print("All 3 models updated successfully with Horizontal Flip / Miroir Droite-Gauche!")

