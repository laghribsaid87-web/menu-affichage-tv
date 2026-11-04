/**
 * STUDIO EDITOR UNIVERSAL V3.5 - TOTAL CONTROL SUITE
 * Drag & Drop, Mouse Wheel Resize, Layers Devant/Derrière, Mirror Flip, Duplicate, Persistent Save
 * Works across all 20 Mon Bocadillo Tanger Menus.
 */
(function() {
    const urlParams = new URLSearchParams(window.location.search);
    const isTvMode = urlParams.get('mode') === 'tv' || document.body.classList.contains('tv-mode') || document.body.classList.contains('tv-display-mode');

    // 1. Inject Editor Styles
    if (!document.getElementById('studio-editor-styles')) {
        const styleEl = document.createElement('style');
        styleEl.id = 'studio-editor-styles';
        styleEl.textContent = `
.editable-item {
            cursor: grab !important;
            user-select: none !important;
            -webkit-user-select: none !important;
            -webkit-user-drag: none !important;
            position: relative;
            transition: outline 0.15s ease, box-shadow 0.15s ease !important;
        }
        .editable-item:hover {
            outline: 2px dashed #f59e0b !important;
            outline-offset: 4px;
        }
        .editable-item.item-selected {
            outline: 3px solid #10b981 !important;
            outline-offset: 5px;
            box-shadow: 0 0 25px rgba(16, 185, 129, 0.6) !important;
        }

        /* Floating Studio Toolbar */
        #studio-floating-bar {
            position: fixed;
            display: none;
            z-index: 99999999;
            background: rgba(15, 23, 42, 0.98);
            border: 2px solid #10b981;
            border-radius: 40px;
            padding: 8px 18px;
            gap: 8px;
            align-items: center;
            box-shadow: 0 15px 40px rgba(0, 0, 0, 0.95), 0 0 25px rgba(16, 185, 129, 0.4);
            backdrop-filter: blur(16px);
            font-family: 'Montserrat', sans-serif;
            animation: barPop 0.2s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            max-width: 95vw;
            flex-wrap: nowrap;
        }
        @keyframes barPop {
            from { transform: scale(0.85); opacity: 0; }
            to { transform: scale(1); opacity: 1; }
        }
        .studio-tag {
            font-size: 11px;
            font-weight: 800;
            color: #fcd535;
            background: rgba(245, 158, 11, 0.15);
            padding: 4px 10px;
            border-radius: 12px;
            border: 1px solid rgba(245, 158, 11, 0.3);
            white-space: nowrap;
            max-width: 150px;
            overflow: hidden;
            text-overflow: ellipsis;
        }
        .studio-btn {
            background: rgba(255, 255, 255, 0.12);
            border: 1px solid rgba(255, 255, 255, 0.25);
            color: #ffffff;
            width: 32px;
            height: 32px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 16px;
            font-weight: 900;
            cursor: pointer;
            transition: all 0.15s ease;
            user-select: none;
            flex-shrink: 0;
        }
        .studio-btn:hover {
            background: #10b981;
            color: #fff;
            transform: scale(1.15);
            border-color: #10b981;
        }
        .studio-val {
            font-family: 'Oswald', sans-serif;
            font-size: 15px;
            font-weight: 900;
            color: #ffffff;
            letter-spacing: 0.5px;
            min-width: 45px;
            text-align: center;
            flex-shrink: 0;
        }
        .studio-pill-btn {
            background: rgba(255, 255, 255, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.2);
            color: #ffffff;
            padding: 5px 10px;
            border-radius: 20px;
            font-size: 11px;
            font-weight: 800;
            cursor: pointer;
            transition: all 0.15s ease;
            white-space: nowrap;
            display: flex;
            align-items: center;
            gap: 4px;
            flex-shrink: 0;
        }
        .studio-pill-btn:hover {
            background: rgba(255, 255, 255, 0.25);
            transform: scale(1.05);
        }
        .studio-pill-btn.btn-front {
            border-color: #10b981;
            color: #6ee7b7;
        }
        .studio-pill-btn.btn-front:hover { background: #10b981; color: #fff; }

        .studio-pill-btn.btn-back {
            border-color: #3b82f6;
            color: #93c5fd;
        }
        .studio-pill-btn.btn-back:hover { background: #3b82f6; color: #fff; }

        
        .studio-pill-btn.btn-flip {
            border-color: #06b6d4;
            color: #67e8f9;
        }
        .studio-pill-btn.btn-flip:hover {
            background: #06b6d4;
            color: #111;
            transform: scale(1.05);
        }

        .studio-pill-btn.btn-dup {
            border-color: #f59e0b;
            color: #fcd34d;
        }
        .studio-pill-btn.btn-dup:hover { background: #f59e0b; color: #111; }

        .studio-pill-btn.btn-del {
            border-color: #ef4444;
            color: #fca5a5;
        }
        .studio-pill-btn.btn-del:hover { background: #ef4444; color: #fff; }

        /* Success Toast */
        #save-toast {
            position: fixed;
            top: 30px;
            left: 50%;
            transform: translateX(-50%) translateY(-100px);
            background: #10b981;
            color: #fff;
            padding: 12px 28px;
            border-radius: 30px;
            font-family: 'Montserrat', sans-serif;
            font-weight: 900;
            font-size: 16px;
            box-shadow: 0 10px 30px rgba(16, 185, 129, 0.5);
            z-index: 999999999;
            transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            display: flex;
            align-items: center;
            gap: 10px;
        }
        #save-toast.visible {
            transform: translateX(-50%) translateY(0);
        }
        `;
        document.head.appendChild(styleEl);
    }

    // 2. Inject Floating Toolbar HTML if not already present
    if (!document.getElementById('studio-floating-bar')) {
        const barWrapper = document.createElement('div');
        barWrapper.innerHTML = `
<div id="studio-floating-bar">
        <span class="studio-tag" id="bar-item-name">&#x2728; lment</span>
        <button class="studio-btn" id="sbar-minus" title="Rduire">&#x2212;</button>
        <span class="studio-val" id="sbar-size-text">100%</span>
        <button class="studio-btn" id="sbar-plus" title="Agrandir">&#x2b;</button>
        <button class="studio-btn" id="sbar-rot-left" title="Pivoter gauche" style="font-size:13px;">&#x21ba;</button>
        <button class="studio-btn" id="sbar-rot-right" title="Pivoter droite" style="font-size:13px;">&#x21bb;</button>
        
        <!-- Devant / Derrire Buttons -->
        <button class="studio-pill-btn btn-front" id="sbar-front" title="Mettre au premier plan (devant)">&#x1f51d; Devant</button>
        <button class="studio-pill-btn btn-back" id="sbar-back" title="Mettre a l'arrire-plan (derrire)">&#x1f96a; Derrire</button>
        
                <!-- Miroir Horizontal (Droite / Gauche) Button -->
        <button class="studio-pill-btn btn-flip" id="sbar-flip" title="Retourner horizontalement (Miroir Droite / Gauche)">🔄 Miroir (↔️)</button>

        <!-- Dupliquer Button -->
        <button class="studio-pill-btn btn-dup" id="sbar-duplicate" title="Dupliquer cet lment">&#x1f4cb; Dupliquer</button>
        
        <!-- Supprimer Button -->
        <button class="studio-pill-btn btn-del" id="sbar-delete" title="Supprimer cet lment">&#x1f5d1;&#xfe0f;</button>
        
        <span style="color:#94a3b8; cursor:pointer; font-size:20px; margin-left:6px;" id="sbar-close">&#x2715;</span>
    </div>
        `;
        document.body.appendChild(barWrapper.firstElementChild);
    }

    // 3. Inject Toast if not present
    if (!document.getElementById('studio-toast')) {
        const toast = document.createElement('div');
        toast.id = 'studio-toast';
        toast.style.cssText = 'position:fixed; bottom:30px; left:50%; transform:translateX(-50%) translateY(100px); background:#10b981; color:#fff; padding:12px 28px; border-radius:30px; font-weight:800; font-size:15px; box-shadow:0 10px 30px rgba(0,0,0,0.8); z-index:999999999; transition:transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275); pointer-events:none; font-family:"Montserrat",sans-serif;';
        toast.textContent = '💾 Disposition enregistrée avec succès !';
        document.body.appendChild(toast);
    }

    // 4. Editor Core Logic
(function() {
        const modelName = window.location.pathname.split('/').pop().replace('.html', '') || 'default';
        const STORAGE_KEY = 'universal_layout_' + modelName;
        let layoutState = {};

        let activeEl = null;
        const bar = document.getElementById('studio-floating-bar');
        const itemName = document.getElementById('bar-item-name');
        const sizeText = document.getElementById('sbar-size-text');
        const toast = document.getElementById('save-toast');

        function getStageScale() {
            const stage = document.getElementById('menu-stage');
            if (!stage) return 1;
            const rect = stage.getBoundingClientRect();
            return (rect.width / 1920) || 1;
        }

        async function loadLayout() {
            try {
                const res = await fetch('/api/get_custom_layout/' + modelName);
                if (res.ok) {
                    const data = await res.json();
                    if (data && Object.keys(data).length > 0) {
                        layoutState = data;
                        applyAllLayout();
                        return;
                    }
                }
            } catch(e) {}

            try {
                layoutState = JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}');
                applyAllLayout();
            } catch(e) {}
        }

        function isFries(el) {
            return el.classList.contains('food-fries') || el.classList.contains('food-fries-side') || el.classList.contains('food-fries-corner');
        }

        function isSandwich(el) {
            return el.classList.contains('food-sandwich');
        }

        function getElementId(el) {
            if (el.dataset.editorId) return el.dataset.editorId;
            const cell = el.closest('.stall-cell, .urban-card, .vibrant-card, .pop-card');
            const cellIdx = cell ? Array.from(cell.parentNode.children).indexOf(cell) : 0;
            const screen = el.closest('.menu-screen');
            const screenId = screen ? screen.id : 's1';
            let type = 'item';
            if (isSandwich(el)) type = 'sandwich';
            else if (isFries(el)) type = 'frites';
            else if (el.classList.contains('title-block') || el.classList.contains('sandwich-name') || el.classList.contains('pop-title')) type = 'title';
            else if (el.classList.contains('price-chalkboard') || el.classList.contains('urban-price-box') || el.classList.contains('price-duo') || el.classList.contains('price-chips')) type = 'price';
            else if (el.classList.contains('ribbon-banner') || el.classList.contains('card-footer') || el.classList.contains('card-ribbon')) type = 'ribbon';

            const id = `${screenId}_c${cellIdx}_${type}`;
            el.dataset.editorId = id;
            return id;
        }

        function applyTransform(el) {
            const s = parseFloat(el.dataset.scale || 1);
            const tx = parseFloat(el.dataset.tx || 0);
            const ty = parseFloat(el.dataset.ty || 0);
            const defaultRot = isFries(el) ? 6 : 0;
            const r = parseFloat(el.dataset.rot !== undefined ? el.dataset.rot : defaultRot);
            const baseShift = isSandwich(el) ? -24 : 0;

            const flipH = parseInt(el.dataset.flipH || '1', 10);
            const transformVal = `translateX(${baseShift + tx}px) translateY(${ty}px) scale(${s * flipH}, ${s}) rotate(${r * flipH}deg)`;
            el.style.setProperty('transform', transformVal, 'important');

            if (el.dataset.zIndex !== undefined) {
                el.style.setProperty('z-index', el.dataset.zIndex, 'important');
            }
        }

        function applyAllLayout() {
            // Apply to existing and handle dynamically cloned items
            Object.keys(layoutState).forEach(id => {
                if (id.includes('_clone_')) {
                    const originalId = id.split('_clone_')[0];
                    const origEl = document.querySelector(`[data-editor-id="${originalId}"]`);
                    if (origEl && !document.querySelector(`[data-editor-id="${id}"]`)) {
                        createCloneElement(origEl, id, layoutState[id]);
                    }
                }
            });

            document.querySelectorAll('.editable-item').forEach(el => {
                const id = getElementId(el);
                if (layoutState[id]) {
                    el.dataset.scale = layoutState[id].scale ?? 1;
                    el.dataset.tx = layoutState[id].x ?? 0;
                    el.dataset.ty = layoutState[id].y ?? 0;
                    el.dataset.rot = layoutState[id].rot ?? (isFries(el) ? 6 : 0);
                    el.dataset.flipH = layoutState[id].flipH ?? 1;
                    if (layoutState[id].zIndex !== undefined) {
                        el.dataset.zIndex = layoutState[id].zIndex;
                    }
                } else {
                    el.dataset.scale = isSandwich(el) ? 1.28 : (isFries(el) ? 1.05 : 1);
                    el.dataset.tx = isSandwich(el) ? -22 : (isFries(el) ? 12 : 0);
                    el.dataset.ty = isSandwich(el) ? 8 : (isFries(el) ? -6 : 0);
                    el.dataset.rot = isFries(el) ? 6 : 0;
                    el.dataset.flipH = 1;
                    el.dataset.zIndex = isFries(el) ? 4 : (isSandwich(el) ? 10 : 20);
                }
                applyTransform(el);
            });
        }

        function saveElementState(el) {
            const id = getElementId(el);
            if (!layoutState[id]) layoutState[id] = {};
            layoutState[id].scale = parseFloat(el.dataset.scale || 1);
            layoutState[id].x = parseFloat(el.dataset.tx || 0);
            layoutState[id].y = parseFloat(el.dataset.ty || 0);
            layoutState[id].rot = parseFloat(el.dataset.rot || (isFries(el) ? 6 : 0));
            layoutState[id].zIndex = el.dataset.zIndex || (isFries(el) ? 4 : (isSandwich(el) ? 10 : 20));
            localStorage.setItem(STORAGE_KEY, JSON.stringify(layoutState));
        }

        function getFriendlyName(el) {
            const cell = el.closest('.stall-cell, .urban-card, .vibrant-card, .pop-card');
            let sandwichName = '';
            if (cell) {
                const t = cell.querySelector('.title-3d, .sandwich-name, .title-block, .pop-title');
                if (t) sandwichName = t.innerText.replace(/\n/g, ' ').trim();
            }
            if (isSandwich(el)) return '&#x1f96a; ' + (sandwichName || 'Sandwich');
            if (isFries(el)) return '&#x1f35f; Frites (' + (sandwichName || '') + ')';
            if (el.classList.contains('title-block') || el.classList.contains('sandwich-name') || el.classList.contains('pop-title')) return '&#x1f3f7;&#xfe0f; Titre: ' + (sandwichName || '');
            if (el.classList.contains('price-chalkboard') || el.classList.contains('urban-price-box') || el.classList.contains('price-duo') || el.classList.contains('price-chips')) return '&#x1f4b0; Prix (' + sandwichName + ')';
            if (el.classList.contains('ribbon-banner') || el.classList.contains('card-footer') || el.classList.contains('card-ribbon')) return '&#x1f4dc; Ingrdients';
            return '&#x2728; lment';
        }

        function positionBar(el) {
            if (!el || !bar) return;
            const r = el.getBoundingClientRect();
            bar.style.display = 'flex';
            bar.style.left = Math.max(10, Math.min(window.innerWidth - 650, (r.left + r.width / 2 - 280))) + 'px';
            bar.style.top = Math.max(10, (r.top - 65)) + 'px';
            itemName.innerHTML = getFriendlyName(el);
            const s = parseFloat(el.dataset.scale || 1);
            sizeText.innerText = Math.round(s * 100) + '%';
        }

        function selectElement(el) {
            document.querySelectorAll('.editable-item').forEach(i => i.classList.remove('item-selected'));
            if (!el) {
                activeEl = null;
                bar.style.display = 'none';
                return;
            }
            activeEl = el;
            el.classList.add('item-selected');
            positionBar(el);
        }

        function bindEditableElement(el) {
            el.classList.add('editable-item');
            getElementId(el);

            el.addEventListener('click', (e) => {
                e.stopPropagation();
                selectElement(el);
            });

            el.addEventListener('wheel', (e) => {
                e.preventDefault();
                e.stopPropagation();
                selectElement(el);

                let s = parseFloat(el.dataset.scale || 1);
                if (e.deltaY < 0) s = Math.min(2.5, s + 0.05);
                else s = Math.max(0.3, s - 0.05);

                el.dataset.scale = s.toFixed(2);
                applyTransform(el);
                saveElementState(el);
                positionBar(el);
            }, { passive: false });
        }

        function createCloneElement(origEl, newId, savedProps) {
            const clone = origEl.cloneNode(true);
            clone.dataset.editorId = newId;
            if (savedProps) {
                clone.dataset.scale = savedProps.scale;
                clone.dataset.tx = savedProps.x;
                clone.dataset.ty = savedProps.y;
                clone.dataset.rot = savedProps.rot;
                clone.dataset.flipH = savedProps.flipH || 1;
                clone.dataset.zIndex = savedProps.zIndex;
            } else {
                clone.dataset.tx = (parseFloat(origEl.dataset.tx || 0) + 30);
                clone.dataset.ty = (parseFloat(origEl.dataset.ty || 0) + 20);
                clone.dataset.zIndex = 26; // place clone on top
            }
            origEl.parentNode.appendChild(clone);
            bindEditableElement(clone);
            applyTransform(clone);
            return clone;
        }

        function initEditor() {
            // Target Sandwich, Frites, Titres, Prix, Ingrdients
            const selector = [
                '.food-sandwich', '.food-fries', '.food-fries-side', '.food-fries-corner',
                '.hero-sandwich-img', '.hero-side-fries', '.hero-side-sauces', '.hero-slate-base', '.hero-platter-group',
                '.canva-hero-title-box', '.canva-callout-badge', '.comic-hero-title-box', '.chalk-callout-1', '.chalk-badge',
                '.title-block', '.sandwich-name', '.pop-title', '.price-chalkboard', '.urban-price-box', '.price-duo',
                '.ribbon-banner', '.card-footer', '.card-ribbon', '.price-pill', '.price-badge', '.price-tag',
                '.menu-card', '.glass-acrylic-card', '.slate-card', '.dish-card', '.col-card', '.item-card', '.sandwich-card',
                '.menu-item-row', '.card-header-bar', '.card-footer-banner',
                'img[src*="cutouts"]', 'img[src*="processed_images"]'
            ].join(', ');
            document.querySelectorAll(selector).forEach(bindEditableElement);
            loadLayout();
        }

        // Toolbar Buttons [+] & [-]
        document.getElementById('sbar-plus').addEventListener('click', (e) => {
            e.stopPropagation();
            if (!activeEl) return;
            let s = parseFloat(activeEl.dataset.scale || 1);
            s = Math.min(2.5, s + 0.08);
            activeEl.dataset.scale = s.toFixed(2);
            applyTransform(activeEl);
            saveElementState(activeEl);
            positionBar(activeEl);
        });

        document.getElementById('sbar-minus').addEventListener('click', (e) => {
            e.stopPropagation();
            if (!activeEl) return;
            let s = parseFloat(activeEl.dataset.scale || 1);
            s = Math.max(0.3, s - 0.08);
            activeEl.dataset.scale = s.toFixed(2);
            applyTransform(activeEl);
            saveElementState(activeEl);
            positionBar(activeEl);
        });

        // Rotation
        document.getElementById('sbar-rot-left').addEventListener('click', (e) => {
            e.stopPropagation();
            if (!activeEl) return;
            let r = parseFloat(activeEl.dataset.rot || 0);
            r -= 3;
            activeEl.dataset.rot = r;
            applyTransform(activeEl);
            saveElementState(activeEl);
        });

        document.getElementById('sbar-rot-right').addEventListener('click', (e) => {
            e.stopPropagation();
            if (!activeEl) return;
            let r = parseFloat(activeEl.dataset.rot || 0);
            r += 3;
            activeEl.dataset.rot = r;
            applyTransform(activeEl);
            saveElementState(activeEl);
        });

        // Mettre Devant (Z-index 25)
        document.getElementById('sbar-front').addEventListener('click', (e) => {
            e.stopPropagation();
            if (!activeEl) return;
            activeEl.dataset.zIndex = 25;
            applyTransform(activeEl);
            saveElementState(activeEl);
            positionBar(activeEl);
        });

        // Mettre Derrire (Z-index 4)
        document.getElementById('sbar-back').addEventListener('click', (e) => {
            e.stopPropagation();
            if (!activeEl) return;
            activeEl.dataset.zIndex = 4;
            applyTransform(activeEl);
            saveElementState(activeEl);
            positionBar(activeEl);
        });

        // DUPLIQUER (Clone Element)
        document.getElementById('sbar-duplicate').addEventListener('click', (e) => {
            e.stopPropagation();
            if (!activeEl) return;
            const newId = getElementId(activeEl) + '_clone_' + Date.now();
            const clone = createCloneElement(activeEl, newId);
            saveElementState(clone);
            selectElement(clone);
        });

        // SUPPRIMER (Delete Element)
        document.getElementById('sbar-delete').addEventListener('click', (e) => {
            e.stopPropagation();
            if (!activeEl) return;
            const id = getElementId(activeEl);
            delete layoutState[id];
            localStorage.setItem(STORAGE_KEY, JSON.stringify(layoutState));
            const toRemove = activeEl;
            selectElement(null);
            toRemove.remove();
        });

        document.getElementById('sbar-close').addEventListener('click', (e) => {
            e.stopPropagation();
            selectElement(null);
        });

        document.addEventListener('click', (e) => {
            if (!e.target.closest('#studio-floating-bar') && !e.target.closest('.editable-item') && !e.target.closest('.ui-controls')) {
                selectElement(null);
            }
        });

        // DRAG ENGINE WITH ACCURATE STAGE SCALE
        let isDragging = false;
        let dragEl = null;
        let startX = 0, startY = 0, initTx = 0, initTy = 0;

        window.addEventListener('mousedown', (e) => {
            const el = e.target.closest('.editable-item');
            if (!el || e.target.closest('#studio-floating-bar') || e.target.closest('.ui-controls')) return;
            isDragging = true;
            dragEl = el;
            startX = e.clientX;
            startY = e.clientY;
            initTx = parseFloat(el.dataset.tx || 0);
            initTy = parseFloat(el.dataset.ty || 0);
            el.style.cursor = 'grabbing';
            selectElement(el);
            e.preventDefault();
        });

        window.addEventListener('mousemove', (e) => {
            if (!isDragging || !dragEl) return;
            const stageScale = getStageScale();
            const dx = (e.clientX - startX) / stageScale;
            const dy = (e.clientY - startY) / stageScale;
            dragEl.dataset.tx = initTx + dx;
            dragEl.dataset.ty = initTy + dy;
            applyTransform(dragEl);
            positionBar(dragEl);
        });

        window.addEventListener('mouseup', () => {
            if (isDragging && dragEl) {
                saveElementState(dragEl);
                dragEl.style.cursor = 'grab';
            }
            isDragging = false;
            dragEl = null;
        });

        // Global Save to Server API
        
        // KEYBOARD ARROW NAVIGATION (Flches du clavier + Shift pour dplacement rapide)
        window.addEventListener('keydown', (e) => {
            if (!activeEl) return;
            if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;

            const step = e.shiftKey ? 15 : 3;
            let moved = false;
            let tx = parseFloat(activeEl.dataset.tx || 0);
            let ty = parseFloat(activeEl.dataset.ty || 0);

            if (e.key === 'ArrowUp') {
                ty -= step;
                moved = true;
            } else if (e.key === 'ArrowDown') {
                ty += step;
                moved = true;
            } else if (e.key === 'ArrowLeft') {
                tx -= step;
                moved = true;
            } else if (e.key === 'ArrowRight') {
                tx += step;
                moved = true;
            } else if (e.key === '+' || e.key === '=') {
                let s = parseFloat(activeEl.dataset.scale || 1);
                s = Math.min(2.5, s + 0.05);
                activeEl.dataset.scale = s.toFixed(2);
                applyTransform(activeEl);
                saveElementState(activeEl);
                positionBar(activeEl);
                e.preventDefault();
                return;
            } else if (e.key === '-' || e.key === '_') {
                let s = parseFloat(activeEl.dataset.scale || 1);
                s = Math.max(0.3, s - 0.05);
                activeEl.dataset.scale = s.toFixed(2);
                applyTransform(activeEl);
                saveElementState(activeEl);
                positionBar(activeEl);
                e.preventDefault();
                return;
                        } else if (e.key === 'm' || e.key === 'M' || e.key === 'h' || e.key === 'H') {
                const currentFlip = parseInt(activeEl.dataset.flipH || '1', 10);
                activeEl.dataset.flipH = (currentFlip === 1) ? -1 : 1;
                applyTransform(activeEl);
                saveElementState(activeEl);
                positionBar(activeEl);
                e.preventDefault();
                return;
            } else if (e.key === 'Escape') {
                selectElement(null);
                e.preventDefault();
                return;
            }

            if (moved) {
                e.preventDefault();
                activeEl.dataset.tx = tx;
                activeEl.dataset.ty = ty;
                applyTransform(activeEl);
                saveElementState(activeEl);
                positionBar(activeEl);
            }
        });

        window.saveLayoutToServer = async function() {
            try {
                const res = await fetch('/api/save_custom_layout', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        model: modelName,
                        layout: layoutState
                    })
                });
                if (res.ok) {
                    toast.classList.add('visible');
                    setTimeout(() => toast.classList.remove('visible'), 3500);
                } else {
                    alert("Erreur lors de la sauvegarde sur le serveur.");
                }
            } catch(e) {
                alert("Erreur rseau: " + e.message);
            }
        };

        window.resetAllLayout = function() {
            if (confirm("Voulez-vous rinitialiser toutes les positions et tailles par dfaut ?")) {
                localStorage.removeItem(STORAGE_KEY);
                layoutState = {};
                applyAllLayout();
                window.saveLayoutToServer();
                selectElement(null);
            }
        };

        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', initEditor);
        } else {
            initEditor();
        }
    })();

})();
