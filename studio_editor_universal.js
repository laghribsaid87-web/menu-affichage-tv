/**
 * STUDIO EDITOR UNIVERSAL V5.0 - TOTAL CONTROL & ONE-CLICK PRICE CHANGER SUITE
 * 1. 1-CLIC ou Double-clic sur N'IMPORTE QUELLE étiquette de prix (kraft-tag, price-sand-num, etc.) pour ouvrir le Modal de Prix
 * 2. Synchronisation automatique et PERMANENTE avec menu_items.json (/api/update_item_price)
 * 3. Diffusion en direct sur toutes les TV (BroadcastChannel MENU_TV_CHANNEL)
 * 4. Déplacement (Drag & Drop) de l'étiquette complète sans détacher les chiffres du fond kraft
 * 5. Molette de la souris pour agrandir / rétrécir n'importe quelle étiquette ou produit
 * 6. Double-clic sur n'importe quel texte pour modifier directement au clavier
 * 7. Sauvegarde permanente sur le serveur (/api/save_custom_layout)
 * Works across ALL 22 Mon Bocadillo Tanger Menus.
 */
(function() {
    const urlParams = new URLSearchParams(window.location.search);
    const isTvMode = urlParams.get('mode') === 'tv' || document.body.classList.contains('tv-mode') || document.body.classList.contains('tv-display-mode');
    const modelName = window.location.pathname.split('/').pop().replace('.html', '') || 'default';
    const STORAGE_KEY = 'universal_layout_' + modelName;

    let layoutState = {};
    let activeEl = null;

    // 1. Inject Styles
    if (!document.getElementById('studio-editor-styles')) {
        const styleEl = document.createElement('style');
        styleEl.id = 'studio-editor-styles';
        styleEl.textContent = `
            .editable-item {
                cursor: grab !important;
                user-select: none !important;
                -webkit-user-select: none !important;
                position: relative;
                transition: outline 0.15s ease, box-shadow 0.15s ease !important;
            }
            .editable-item:hover {
                outline: 2px dashed #f59e0b !important;
                outline-offset: 3px;
            }
            .editable-item.item-selected {
                outline: 3px solid #10b981 !important;
                outline-offset: 4px;
                box-shadow: 0 0 25px rgba(16, 185, 129, 0.6) !important;
            }
            .text-editing-active {
                outline: 3px solid #00f0ff !important;
                background: rgba(0, 240, 255, 0.22) !important;
                border-radius: 6px;
                cursor: text !important;
                user-select: text !important;
                -webkit-user-select: text !important;
            }

            /* Price tag hover indicator */
            .kraft-tag, .price-sand-num, .price-drk-num, .canva-badge-price, .ciel-price-tag, .spec-price-tag, .price-capsule {
                cursor: pointer !important;
            }

            /* Floating Studio Toolbar */
            #studio-floating-bar {
                position: fixed;
                display: none;
                z-index: 99999999;
                background: rgba(15, 23, 42, 0.98);
                border: 2px solid #10b981;
                border-radius: 40px;
                padding: 7px 16px;
                gap: 8px;
                align-items: center;
                box-shadow: 0 15px 40px rgba(0, 0, 0, 0.95), 0 0 25px rgba(16, 185, 129, 0.4);
                backdrop-filter: blur(16px);
                font-family: 'Montserrat', system-ui, sans-serif;
                animation: barPop 0.2s cubic-bezier(0.175, 0.885, 0.32, 1.275);
                max-width: 96vw;
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
                max-width: 140px;
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
                font-size: 15px;
                font-weight: 900;
                cursor: pointer;
                transition: all 0.15s ease;
                user-select: none;
                flex-shrink: 0;
            }
            .studio-btn:hover {
                background: #10b981;
                color: #000;
                border-color: #10b981;
                transform: scale(1.15);
            }
            .studio-btn-wide {
                width: auto !important;
                padding: 0 12px !important;
                border-radius: 20px !important;
                font-size: 12px !important;
                gap: 5px;
            }
            .studio-btn-price {
                background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%) !important;
                color: #000 !important;
                border-color: #fbbf24 !important;
                font-weight: 900 !important;
                box-shadow: 0 0 12px rgba(245, 158, 11, 0.5) !important;
            }
            .studio-btn-price:hover {
                background: #fbbf24 !important;
                transform: scale(1.08) !important;
            }
            .studio-btn-save {
                background: linear-gradient(135deg, #10b981 0%, #059669 100%);
                color: #ffffff;
                border: 1px solid #34d399;
                font-weight: 900;
                box-shadow: 0 0 15px rgba(16, 185, 129, 0.4);
            }
            .studio-btn-save:hover {
                background: #34d399;
                color: #000;
                transform: scale(1.08);
            }
            .studio-divider {
                width: 1px;
                height: 20px;
                background: rgba(255, 255, 255, 0.2);
                margin: 0 2px;
            }

            /* TV Mode override */
            body.tv-mode .editable-item,
            body.tv-display-mode .editable-item {
                cursor: default !important;
                outline: none !important;
                box-shadow: none !important;
            }
            body.tv-mode #studio-floating-bar,
            body.tv-display-mode #studio-floating-bar,
            body.tv-mode #studio-price-modal,
            body.tv-display-mode #studio-price-modal {
                display: none !important;
            }
        `;
        document.head.appendChild(styleEl);
    }

    // 2. Inject Toolbar HTML
    if (!document.getElementById('studio-floating-bar')) {
        const bar = document.createElement('div');
        bar.id = 'studio-floating-bar';
        bar.innerHTML = `
            <span class="studio-tag" id="sbar-tag">ÉLÉMENT</span>
            <div class="studio-divider"></div>
            <!-- Quick Price Edit Button -->
            <button class="studio-btn studio-btn-wide studio-btn-price" id="sbar-edit-price" title="Modifier le prix de cet article (ou clic direct sur le prix)">💰 Modifier Prix</button>
            <!-- Edit Text Button -->
            <button class="studio-btn studio-btn-wide" id="sbar-edit-text" title="Modifier le texte (ou double-clic)">✏️ Texte</button>
            <div class="studio-divider"></div>
            <!-- Scale +/- -->
            <button class="studio-btn" id="sbar-plus" title="Agrandir (+)">＋</button>
            <button class="studio-btn" id="sbar-minus" title="Rétrécir (-)">－</button>
            <div class="studio-divider"></div>
            <!-- Layers Devant/Derrière -->
            <button class="studio-btn" id="sbar-devant" title="Mettre Devant (Calque +)">⬆</button>
            <button class="studio-btn" id="sbar-derriere" title="Mettre Derrière (Calque -)">⬇</button>
            <div class="studio-divider"></div>
            <!-- Flip & Rotate -->
            <button class="studio-btn" id="sbar-flip" title="Miroir Horizontal">⇦⇨</button>
            <button class="studio-btn" id="sbar-rot-left" title="Pivoter Gauche">⤾</button>
            <button class="studio-btn" id="sbar-rot-right" title="Pivoter Droite">⤿</button>
            <div class="studio-divider"></div>
            <!-- Duplicate & Reset -->
            <button class="studio-btn" id="sbar-duplicate" title="Dupliquer">📋</button>
            <button class="studio-btn" id="sbar-reset" title="Réinitialiser">↺</button>
            <div class="studio-divider"></div>
            <!-- Save Button -->
            <button class="studio-btn studio-btn-wide studio-btn-save" id="sbar-save" title="Enregistrer sur le serveur">💾 Enregistrer</button>
        `;
        document.body.appendChild(bar);
    }

    // 3. Inject Toast
    if (!document.getElementById('studio-toast')) {
        const toast = document.createElement('div');
        toast.id = 'studio-toast';
        toast.style.cssText = 'position:fixed; bottom:30px; left:50%; transform:translateX(-50%) translateY(120px); background:#10b981; color:#fff; padding:12px 28px; border-radius:30px; font-weight:800; font-size:15px; box-shadow:0 10px 30px rgba(0,0,0,0.8); z-index:999999999; transition:transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275); pointer-events:none; font-family:"Montserrat",sans-serif;';
        toast.textContent = '💾 Disposition et textes enregistrés !';
        document.body.appendChild(toast);
    }

    function showToast(msg) {
        const t = document.getElementById('studio-toast');
        if (!t) return;
        if (msg) t.textContent = msg;
        t.style.transform = 'translateX(-50%) translateY(0)';
        setTimeout(() => {
            t.style.transform = 'translateX(-50%) translateY(120px)';
        }, 3000);
    }

    // 4. Inject Fast Price Modal HTML
    if (!document.getElementById('studio-price-modal')) {
        const modal = document.createElement('div');
        modal.id = 'studio-price-modal';
        modal.style.cssText = `
            display: none;
            position: fixed;
            inset: 0;
            z-index: 9999999999;
            background: rgba(10, 15, 26, 0.88);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            align-items: center;
            justify-content: center;
            font-family: 'Montserrat', system-ui, sans-serif;
        `;
        modal.innerHTML = `
            <div style="background:#111827; border:2px solid #f59e0b; border-radius:24px; padding:28px 32px; width:92%; max-width:440px; box-shadow:0 25px 60px rgba(0,0,0,0.95), 0 0 40px rgba(245,158,11,0.25); color:#fff; position:relative; box-sizing:border-box;">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:20px; border-bottom:1px solid rgba(255,255,255,0.1); padding-bottom:14px;">
                    <div style="display:flex; align-items:center; gap:12px;">
                        <div style="width:42px; height:42px; border-radius:14px; background:rgba(245,158,11,0.18); border:1px solid #f59e0b; display:flex; align-items:center; justify-content:center; font-size:22px;">💰</div>
                        <div>
                            <h3 id="modal-item-name" style="margin:0; font-size:18px; font-weight:900; color:#fbbf24; text-transform:uppercase; letter-spacing:0.5px;">MODIFIER LE PRIX</h3>
                            <div id="modal-item-category" style="font-size:12px; font-weight:700; color:#9ca3af; margin-top:2px;">Mon Bocadillo Tanger</div>
                        </div>
                    </div>
                    <button id="modal-close-btn" type="button" style="background:rgba(255,255,255,0.1); border:1px solid rgba(255,255,255,0.15); color:#9ca3af; width:34px; height:34px; border-radius:50%; font-size:18px; cursor:pointer; font-weight:bold; display:flex; align-items:center; justify-content:center; transition:all 0.15s;">&times;</button>
                </div>

                <form id="studio-price-form" onsubmit="return false;" style="display:flex; flex-direction:column; gap:18px; margin:0;">
                    <div>
                        <label style="display:block; font-size:12px; font-weight:800; color:#e5e7eb; margin-bottom:8px; text-transform:uppercase; letter-spacing:0.5px;">
                            🥪 Prix Sandwich / Plat (DH) :
                        </label>
                        <div style="position:relative; display:flex; align-items:center;">
                            <input id="modal-sand-price" type="number" step="0.5" min="0" required style="width:100%; box-sizing:border-box; background:#1f2937; border:2px solid #374151; border-radius:14px; padding:12px 60px 12px 18px; font-size:24px; font-weight:900; color:#10b981; outline:none; transition:border-color 0.2s;" placeholder="ex: 30">
                            <span style="position:absolute; right:18px; font-size:15px; font-weight:900; color:#9ca3af; pointer-events:none;">DH</span>
                        </div>
                    </div>

                    <div>
                        <label style="display:block; font-size:12px; font-weight:800; color:#e5e7eb; margin-bottom:8px; text-transform:uppercase; letter-spacing:0.5px;">
                            🥤 Option Boisson Fraîche (DH) :
                        </label>
                        <div style="position:relative; display:flex; align-items:center;">
                            <input id="modal-drk-price" type="number" step="0.5" min="0" required style="width:100%; box-sizing:border-box; background:#1f2937; border:2px solid #374151; border-radius:14px; padding:12px 60px 12px 18px; font-size:24px; font-weight:900; color:#f59e0b; outline:none; transition:border-color 0.2s;" placeholder="ex: 7">
                            <span style="position:absolute; right:18px; font-size:15px; font-weight:900; color:#9ca3af; pointer-events:none;">DH</span>
                        </div>
                    </div>

                    <div style="display:flex; gap:12px; margin-top:8px;">
                        <button id="modal-cancel-btn" type="button" style="flex:1; padding:14px; border-radius:14px; background:rgba(255,255,255,0.08); border:1px solid rgba(255,255,255,0.18); color:#e5e7eb; font-weight:800; font-size:13px; cursor:pointer; transition:all 0.15s;">Annuler</button>
                        <button id="modal-save-btn" type="submit" style="flex:2; padding:14px; border-radius:14px; background:linear-gradient(135deg, #10b981 0%, #059669 100%); border:none; color:#ffffff; font-weight:900; font-size:14px; cursor:pointer; box-shadow:0 6px 20px rgba(16,185,129,0.4); transition:all 0.15s;">💾 Enregistrer Partout</button>
                    </div>
                </form>
            </div>
        `;
        document.body.appendChild(modal);
    }

    // 5. Utility Functions
    function getStageScale() {
        const stageEl = document.getElementById('stage') || document.querySelector('.stage') || document.getElementById('screen-stage') || document.body;
        const rect = stageEl.getBoundingClientRect();
        return (rect.width / 1920) || 1;
    }

    function isSandwich(el) {
        const src = (el.src || el.querySelector('img')?.src || '').toLowerCase();
        return src.includes('sandwich') || src.includes('bocadillo') || src.includes('cutout');
    }

    function isFries(el) {
        const src = (el.src || el.querySelector('img')?.src || '').toLowerCase();
        return src.includes('frite') || src.includes('fries') || src.includes('cornet');
    }

    function isPriceOrTag(el) {
        const cls = (el.className || '').toString().toLowerCase();
        return cls.includes('price') || cls.includes('tag') || cls.includes('kraft') || cls.includes('badge') || cls.includes('sand-num') || cls.includes('drk-num') || el.dataset?.priceRole;
    }

    function getItemDataFromElement(el) {
        const card = el.closest('[data-item-id], .menu-card, .glass-acrylic-card, .slate-card, .dish-card, .col-card, .item-card, .sandwich-card, .menu-item-row') || el;
        
        let itemId = card.dataset?.itemId || el.dataset?.itemId || '';
        
        let title = '';
        const titleEl = card.querySelector?.('.main-title, .brand-title, .canva-hero-title, .item-title, .sandwich-name, h1, h2, h3, h4');
        if (titleEl) {
            title = (titleEl.innerText || '').trim();
        }
        
        if (!itemId && title) {
            itemId = title.toLowerCase().replace(/[^a-z0-9]/g, '_');
        }
        if (!itemId) itemId = 'complet';

        let sandPrice = '30';
        const sandPriceEl = card.querySelector?.('.price-sand-num, .canva-price-val, .ciel-price-num, .price-val, .price-num, .p-sand-val, .p-sand') || el.closest?.('.price-sand-num, .canva-price-val, .ciel-price-num, .price-val, .price-num') || el;
        if (sandPriceEl) {
            const raw = sandPriceEl.innerText || '';
            const m = raw.match(/(\d+(?:[.,]\d+)?)/);
            if (m) sandPrice = m[1];
        }

        let drkPrice = '7';
        const drkPriceEl = card.querySelector?.('.price-drk-num, .p-drk-val, .p-drk') || el.closest?.('.price-drk-num');
        if (drkPriceEl) {
            const raw = drkPriceEl.innerText || '';
            const m = raw.match(/(\d+(?:[.,]\d+)?)/);
            if (m) drkPrice = m[1];
        }

        return { card, itemId, title: title || itemId.toUpperCase(), sandPrice, drkPrice, sandPriceEl, drkPriceEl };
    }

    // Modal Control Functions
    let currentModalTarget = null;

    function openPriceModal(targetEl) {
        if (isTvMode) return;
        const modal = document.getElementById('studio-price-modal');
        if (!modal) return;

        currentModalTarget = getItemDataFromElement(targetEl);

        document.getElementById('modal-item-name').textContent = currentModalTarget.title;
        document.getElementById('modal-item-category').textContent = `Article: ${currentModalTarget.itemId.toUpperCase()} • Mon Bocadillo Tanger`;
        
        const sandInput = document.getElementById('modal-sand-price');
        const drkInput = document.getElementById('modal-drk-price');
        
        sandInput.value = currentModalTarget.sandPrice;
        drkInput.value = currentModalTarget.drkPrice;

        modal.style.display = 'flex';
        setTimeout(() => {
            sandInput.focus();
            sandInput.select();
        }, 50);
    }

    function closePriceModal() {
        const modal = document.getElementById('studio-price-modal');
        if (modal) modal.style.display = 'none';
        currentModalTarget = null;
    }

    async function saveItemPrice(itemId, newSandPrice, newDrkPrice, itemData) {
        newSandPrice = (newSandPrice || '').toString().trim();
        newDrkPrice = (newDrkPrice || '').toString().trim().replace(/^\+/, '');

        // 1. Update DOM Elements
        if (itemData && itemData.card) {
            const card = itemData.card;
            
            const pSand = card.querySelector('.price-sand-num, .p-sand-val, .p-sand, .canva-price-val, .ciel-price-num, .price-val, .price-num');
            if (pSand) {
                const currSpan = pSand.querySelector('span');
                const currClass = currSpan && currSpan.className ? currSpan.className : 'curr';
                pSand.innerHTML = `${newSandPrice}<span class="${currClass}">DH</span>`;
                pSand.dataset.hasCustomText = 'true';
            }

            const pDrk = card.querySelector('.price-drk-num, .p-drk-val, .p-drk');
            if (pDrk) {
                const currSpan = pDrk.querySelector('span');
                const currClass = currSpan && currSpan.className ? currSpan.className : 'curr';
                const hasPrefix = pDrk.innerText.toLowerCase().includes('boisson') ? '+BOISSON ' : (pDrk.innerText.toLowerCase().includes('soda') ? '+SODA ' : '');
                pDrk.innerHTML = `${hasPrefix}+${newDrkPrice}<span class="${currClass}">DH</span>`;
                pDrk.dataset.hasCustomText = 'true';
            }

            const tag = card.querySelector('.kraft-tag, .ciel-price-tag, .canva-callout-badge, .price-box');
            if (tag) tag.dataset.hasCustomText = 'true';
        }

        // 2. Send to Backend API
        try {
            const res = await fetch('/api/update_item_price', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    id: itemId,
                    price_sandwich: newSandPrice,
                    price_drink: `+${newDrkPrice}`
                })
            });

            if (res.ok) {
                const json = await res.json();
                
                // 3. Update localStorage cache
                if (json.data) {
                    try {
                        localStorage.setItem('MENU_ITEMS_CACHE', JSON.stringify(json.data));
                    } catch(e) {}

                    // 4. Broadcast to TV Channel
                    if (window.BroadcastChannel) {
                        try {
                            const bc = new BroadcastChannel('MENU_TV_CHANNEL');
                            bc.postMessage({ type: 'PRICES_UPDATED', data: json.data });
                        } catch(e) {}
                    }
                }
            }
        } catch(e) {
            console.warn("Server price sync failed:", e);
        }

        // 5. Save Custom Layout
        if (window.saveLayoutToServer) {
            window.saveLayoutToServer();
        }

        // 6. Show Toast
        showToast(`💰 Prix enregistré : ${newSandPrice} DH (+${newDrkPrice} DH Boisson) !`);
    }

    // Bind Modal Events
    document.getElementById('studio-price-form')?.addEventListener('submit', async (e) => {
        e.preventDefault();
        if (!currentModalTarget) return;

        const sandVal = document.getElementById('modal-sand-price').value;
        const drkVal = document.getElementById('modal-drk-price').value;

        await saveItemPrice(currentModalTarget.itemId, sandVal, drkVal, currentModalTarget);
        closePriceModal();
    });

    document.getElementById('modal-close-btn')?.addEventListener('click', closePriceModal);
    document.getElementById('modal-cancel-btn')?.addEventListener('click', closePriceModal);
    
    document.getElementById('studio-price-modal')?.addEventListener('click', (e) => {
        if (e.target.id === 'studio-price-modal') closePriceModal();
    });

    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            const modal = document.getElementById('studio-price-modal');
            if (modal && modal.style.display === 'flex') closePriceModal();
        }
    });

    // 6. Get Unique Element ID for State
    function getElementId(el) {
        if (el.dataset.editorId) return el.dataset.editorId;

        const screen = el.closest('.menu-screen, .scene-view, [id^="screen"], [id^="scene"]');
        const screenId = screen ? screen.id : 's1';
        const itemId = el.dataset.itemId || el.closest('[data-item-id]')?.dataset.itemId;

        let id = '';
        if (el.id) {
            id = el.id;
        } else if (itemId) {
            const subType = el.className.split(/\s+/)[0] || 'part';
            id = `${screenId}_${itemId}_${subType}`;
        } else {
            const tag = el.tagName.toLowerCase();
            const cleanClass = (el.className || '').replace(/editable-item|item-selected|text-editing-active/g, '').trim().split(/\s+/)[0] || 'node';
            const allMatches = document.querySelectorAll(`${tag}.${cleanClass}`);
            const pos = Array.from(allMatches).indexOf(el);
            id = `${screenId}_${tag}_${cleanClass}_${pos >= 0 ? pos : 0}`;
        }

        el.dataset.editorId = id;
        return id;
    }

    function applyTransform(el) {
        const tx = parseFloat(el.dataset.tx || 0);
        const ty = parseFloat(el.dataset.ty || 0);
        const s = parseFloat(el.dataset.scale || 1);
        const r = parseFloat(el.dataset.rot || 0);
        const flipH = parseFloat(el.dataset.flipH || 1);
        const z = el.dataset.zIndex || '';

        const baseShift = el.classList.contains('food-fries-corner') ? 40 : 0;
        const transformStr = `translateX(${baseShift + tx}px) translateY(${ty}px) scale(${s * flipH}, ${s}) rotate(${r * flipH}deg)`;
        el.style.setProperty('transform', transformStr, 'important');
        if (z) el.style.setProperty('z-index', z, 'important');

        if (window.getComputedStyle(el).display === 'inline') {
            el.style.setProperty('display', 'inline-block', 'important');
        }
        if (s !== 1 || tx !== 0 || ty !== 0) {
            el.style.setProperty('animation', 'none', 'important');
        }
    }

    function saveElementState(el) {
        const id = getElementId(el);
        if (!layoutState[id]) layoutState[id] = {};
        layoutState[id].x = parseFloat(el.dataset.tx || 0);
        layoutState[id].y = parseFloat(el.dataset.ty || 0);
        layoutState[id].scale = parseFloat(el.dataset.scale || 1);
        layoutState[id].rot = parseFloat(el.dataset.rot || 0);
        layoutState[id].flipH = parseFloat(el.dataset.flipH || 1);
        layoutState[id].zIndex = el.dataset.zIndex || '';

        if (el.dataset.hasCustomText === 'true') {
            layoutState[id].customHtml = el.innerHTML;
        }

        try {
            localStorage.setItem(STORAGE_KEY, JSON.stringify(layoutState));
        } catch(e) {}
    }

    function applyAllLayout() {
        Object.keys(layoutState).forEach(id => {
            let el = document.querySelector(`[data-editor-id="${id}"]`);
            if (!el) el = document.getElementById(id);
            if (el) {
                const data = layoutState[id];
                if (data.x !== undefined) el.dataset.tx = data.x;
                if (data.y !== undefined) el.dataset.ty = data.y;
                if (data.scale !== undefined) el.dataset.scale = data.scale;
                if (data.rot !== undefined) el.dataset.rot = data.rot;
                if (data.flipH !== undefined) el.dataset.flipH = data.flipH;
                if (data.zIndex !== undefined) el.dataset.zIndex = data.zIndex;

                if (data.customHtml !== undefined) {
                    el.innerHTML = data.customHtml;
                    el.dataset.hasCustomText = 'true';
                }
                applyTransform(el);
            }
        });
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
            const saved = localStorage.getItem(STORAGE_KEY);
            if (saved) {
                layoutState = JSON.parse(saved);
                applyAllLayout();
            }
        } catch(e) {}
    }

    function getFriendlyName(el) {
        if (isSandwich(el)) return '🥪 Sandwich';
        if (isFries(el)) return '🍟 Frites';
        if (isPriceOrTag(el)) return '🏷️ Prix / Tag';
        if (el.tagName.match(/^H[1-6]$/)) return '📝 Titre';
        if (el.classList.contains('desc') || el.tagName === 'P') return '📄 Description';
        if (el.tagName === 'SPAN') return '🏷️ Texte/Badge';
        return '📦 Élément';
    }

    const bar = document.getElementById('studio-floating-bar');

    function positionBar(el) {
        if (!bar || isTvMode) return;
        const rect = el.getBoundingClientRect();
        let top = rect.top - 62;
        if (top < 12) top = rect.bottom + 14;
        let left = rect.left + (rect.width / 2) - (bar.offsetWidth / 2);
        left = Math.max(16, Math.min(window.innerWidth - bar.offsetWidth - 16, left));

        bar.style.top = `${top}px`;
        bar.style.left = `${left}px`;
        bar.style.display = 'flex';
    }

    function selectElement(el) {
        if (isTvMode) return;
        document.querySelectorAll('.editable-item').forEach(i => i.classList.remove('item-selected'));
        activeEl = el;
        el.classList.add('item-selected');

        const tag = document.getElementById('sbar-tag');
        if (tag) tag.textContent = getFriendlyName(el);

        const priceBtn = document.getElementById('sbar-edit-price');
        if (priceBtn) {
            priceBtn.style.display = isPriceOrTag(el) || el.closest('[data-item-id]') || el.querySelector('.price-sand-num, .price-num, .price-val') ? 'inline-flex' : 'none';
        }

        positionBar(el);
    }

    // 7. INLINE TEXT EDITING ENGINE
    function startTextEditing(el) {
        if (isTvMode || el.tagName === 'IMG') return;

        el.contentEditable = 'true';
        el.classList.add('text-editing-active');
        el.focus();

        const range = document.createRange();
        range.selectNodeContents(el);
        const sel = window.getSelection();
        sel.removeAllRanges();
        sel.addRange(range);

        function finishEdit() {
            el.contentEditable = 'false';
            el.classList.remove('text-editing-active');
            el.removeEventListener('blur', finishEdit);
            el.removeEventListener('keydown', onKeyDown);

            el.dataset.hasCustomText = 'true';
            saveElementState(el);
            showToast("✏️ Modifié et enregistré !");
            positionBar(el);
        }

        function onKeyDown(e) {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                el.blur();
            } else if (e.key === 'Escape') {
                if (el.dataset.origHtml) el.innerHTML = el.dataset.origHtml;
                el.blur();
            }
        }

        el.addEventListener('blur', finishEdit);
        el.addEventListener('keydown', onKeyDown);
    }

    // 8. BIND EDITABLE ELEMENT
    function bindEditableElement(el) {
        // Tag Child Interceptor: If this element is inside a parent price container (like .kraft-tag),
        // let the parent handle dragging & scaling so the numbers don't break off the kraft tag,
        // but let clicking on the number open the price modal!
        const parentTag = el.parentElement?.closest?.('.kraft-tag, .ciel-price-tag, .canva-badge-card, .canva-callout-badge, .gold-price-box, .neon-price-box, .fire-price, .bento-price, .spec-price-tag, .price-capsule, .price-circle-badge, .price-box, .urban-price-box');
        if (parentTag && parentTag !== el) {
            el.addEventListener('click', (e) => {
                if (isTvMode) return;
                e.stopPropagation();
                openPriceModal(el);
            });
            return;
        }

        if (el.classList.contains('editable-item')) return;
        el.classList.add('editable-item');
        getElementId(el);

        if (!el.dataset.origHtml && el.tagName !== 'IMG') {
            el.dataset.origHtml = el.innerHTML;
        }

        el.addEventListener('click', (e) => {
            if (el.isContentEditable) return;
            e.stopPropagation();
            selectElement(el);
        });

        el.addEventListener('dblclick', (e) => {
            if (el.tagName !== 'IMG') {
                e.stopPropagation();
                selectElement(el);
                if (isPriceOrTag(el)) {
                    openPriceModal(el);
                } else {
                    startTextEditing(el);
                }
            }
        });

        el.addEventListener('wheel', (e) => {
            if (isTvMode || el.isContentEditable) return;
            e.preventDefault();
            e.stopPropagation();
            selectElement(el);

            let s = parseFloat(el.dataset.scale || 1);
            if (e.deltaY < 0) s = Math.min(3.0, s + 0.05);
            else s = Math.max(0.2, s - 0.05);

            el.dataset.scale = s.toFixed(2);
            applyTransform(el);
            saveElementState(el);
            positionBar(el);
        }, { passive: false });
    }

    // 9. DRAG & DROP ENGINE + CLICK DETECTION
    let isDragging = false;
    let dragEl = null;
    let startX = 0, startY = 0;
    let initTx = 0, initTy = 0;
    let hasMovedMouse = false;

    document.addEventListener('mousedown', (e) => {
        if (isTvMode) return;
        const el = e.target.closest('.editable-item');
        if (!el || el.isContentEditable || e.target.closest('#studio-floating-bar') || e.target.closest('#studio-price-modal') || e.target.closest('.ui-controls') || e.target.closest('.dock-controls')) return;

        isDragging = true;
        dragEl = el;
        hasMovedMouse = false;
        startX = e.clientX;
        startY = e.clientY;
        initTx = parseFloat(el.dataset.tx || 0);
        initTy = parseFloat(el.dataset.ty || 0);
        selectElement(el);
        el.style.cursor = 'grabbing';
    });

    document.addEventListener('mousemove', (e) => {
        if (!isDragging || !dragEl) return;
        if (Math.abs(e.clientX - startX) > 4 || Math.abs(e.clientY - startY) > 4) {
            hasMovedMouse = true;
        }
        const stageScale = getStageScale();
        const dx = (e.clientX - startX) / stageScale;
        const dy = (e.clientY - startY) / stageScale;

        dragEl.dataset.tx = (initTx + dx).toFixed(1);
        dragEl.dataset.ty = (initTy + dy).toFixed(1);
        applyTransform(dragEl);
        positionBar(dragEl);
    });

    document.addEventListener('mouseup', (e) => {
        if (isDragging && dragEl) {
            saveElementState(dragEl);
            dragEl.style.cursor = 'grab';

            // 1-CLIC PRICE DETECTION:
            // If the user clicked on a price tag (without dragging), immediately open the Price Modal!
            if (!hasMovedMouse && isPriceOrTag(dragEl)) {
                openPriceModal(dragEl);
            }
        }
        isDragging = false;
        dragEl = null;
    });

    document.addEventListener('click', (e) => {
        if (!e.target.closest('#studio-floating-bar') && !e.target.closest('#studio-price-modal') && !e.target.closest('.editable-item') && !e.target.closest('.ui-controls') && !e.target.closest('.dock-controls')) {
            document.querySelectorAll('.editable-item').forEach(i => i.classList.remove('item-selected'));
            activeEl = null;
            if (bar) bar.style.display = 'none';
        }
    });

    // 10. TOOLBAR BUTTON LISTENERS
    document.getElementById('sbar-edit-price')?.addEventListener('click', (e) => {
        e.stopPropagation();
        if (!activeEl) return;
        openPriceModal(activeEl);
    });

    document.getElementById('sbar-edit-text')?.addEventListener('click', (e) => {
        e.stopPropagation();
        if (!activeEl) return;
        startTextEditing(activeEl);
    });

    document.getElementById('sbar-plus')?.addEventListener('click', (e) => {
        e.stopPropagation();
        if (!activeEl) return;
        let s = parseFloat(activeEl.dataset.scale || 1);
        s = Math.min(3.0, s + 0.08);
        activeEl.dataset.scale = s.toFixed(2);
        applyTransform(activeEl);
        saveElementState(activeEl);
        positionBar(activeEl);
    });

    document.getElementById('sbar-minus')?.addEventListener('click', (e) => {
        e.stopPropagation();
        if (!activeEl) return;
        let s = parseFloat(activeEl.dataset.scale || 1);
        s = Math.max(0.2, s - 0.08);
        activeEl.dataset.scale = s.toFixed(2);
        applyTransform(activeEl);
        saveElementState(activeEl);
        positionBar(activeEl);
    });

    document.getElementById('sbar-devant')?.addEventListener('click', (e) => {
        e.stopPropagation();
        if (!activeEl) return;
        let z = parseInt(activeEl.dataset.zIndex || window.getComputedStyle(activeEl).zIndex || 10, 10);
        if (isNaN(z)) z = 10;
        z += 5;
        activeEl.dataset.zIndex = z;
        applyTransform(activeEl);
        saveElementState(activeEl);
    });

    document.getElementById('sbar-derriere')?.addEventListener('click', (e) => {
        e.stopPropagation();
        if (!activeEl) return;
        let z = parseInt(activeEl.dataset.zIndex || window.getComputedStyle(activeEl).zIndex || 10, 10);
        if (isNaN(z)) z = 10;
        z = Math.max(1, z - 5);
        activeEl.dataset.zIndex = z;
        applyTransform(activeEl);
        saveElementState(activeEl);
    });

    document.getElementById('sbar-flip')?.addEventListener('click', (e) => {
        e.stopPropagation();
        if (!activeEl) return;
        let flipH = parseFloat(activeEl.dataset.flipH || 1);
        flipH = flipH * -1;
        activeEl.dataset.flipH = flipH;
        applyTransform(activeEl);
        saveElementState(activeEl);
    });

    document.getElementById('sbar-rot-left')?.addEventListener('click', (e) => {
        e.stopPropagation();
        if (!activeEl) return;
        let r = parseFloat(activeEl.dataset.rot || 0);
        r -= 5;
        activeEl.dataset.rot = r;
        applyTransform(activeEl);
        saveElementState(activeEl);
    });

    document.getElementById('sbar-rot-right')?.addEventListener('click', (e) => {
        e.stopPropagation();
        if (!activeEl) return;
        let r = parseFloat(activeEl.dataset.rot || 0);
        r += 5;
        activeEl.dataset.rot = r;
        applyTransform(activeEl);
        saveElementState(activeEl);
    });

    document.getElementById('sbar-duplicate')?.addEventListener('click', (e) => {
        e.stopPropagation();
        if (!activeEl) return;
        const clone = activeEl.cloneNode(true);
        const newId = getElementId(activeEl) + '_copy_' + Date.now().toString(36);
        clone.dataset.editorId = newId;
        clone.dataset.tx = (parseFloat(activeEl.dataset.tx || 0) + 30);
        clone.dataset.ty = (parseFloat(activeEl.dataset.ty || 0) + 20);
        activeEl.parentNode.appendChild(clone);
        bindEditableElement(clone);
        applyTransform(clone);
        saveElementState(clone);
        selectElement(clone);
        showToast("📋 Élément dupliqué avec succès !");
    });

    document.getElementById('sbar-reset')?.addEventListener('click', (e) => {
        e.stopPropagation();
        if (!activeEl) return;
        activeEl.dataset.tx = 0;
        activeEl.dataset.ty = 0;
        activeEl.dataset.scale = isSandwich(activeEl) ? 1.28 : (isFries(activeEl) ? 1.05 : 1);
        activeEl.dataset.rot = 0;
        activeEl.dataset.flipH = 1;
        activeEl.dataset.zIndex = '';

        if (activeEl.dataset.origHtml) {
            activeEl.innerHTML = activeEl.dataset.origHtml;
            delete activeEl.dataset.hasCustomText;
        }
        const id = getElementId(activeEl);
        if (layoutState[id]) {
            delete layoutState[id].customHtml;
        }

        applyTransform(activeEl);
        saveElementState(activeEl);
        positionBar(activeEl);
        showToast("↺ Réinitialisé par défaut !");
    });

    // 11. PERSISTENT SAVE TO SERVER
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
                showToast("💾 Enregistré sur le serveur avec succès !");
            } else {
                showToast("💾 Enregistré localement");
            }
        } catch(e) {
            showToast("💾 Enregistré localement");
        }
    };

    document.getElementById('sbar-save')?.addEventListener('click', (e) => {
        e.stopPropagation();
        window.saveLayoutToServer();
    });

    // 12. INITIALIZE ALL ELEMENTS
    function initEditor() {
        const explicitSelectors = [
            // Food items
            '.food-sandwich', '.food-fries', '.food-fries-side', '.food-fries-corner',
            '.hero-sandwich-img', '.hero-side-fries', '.hero-side-sauces', '.hero-slate-base', '.hero-platter-group',

            // All Price Tag Containers
            '.kraft-tag', '.ciel-price-tag', '.canva-badge-card', '.canva-callout-badge', '.cinema-price-badge',
            '.gold-price-box', '.neon-price-box', '.fire-price', '.bento-price', '.spec-price-tag',
            '.price-capsule', '.price-circle-badge', '.price-box', '.price-container', '.price-row',
            '.price-sticker', '.price-badge-box', '.price-badge-alone', '.price-badge-menu',
            '.hero-price-panel', '.hero-price-row', '.hero-price-tag',
            '.c-val', '.card-tag', '.fries-included-tag', '.promo-tag-banner',
            '.price-num', '.price-cur', '.price-chalkboard', '.urban-price-box', '.price-duo',
            '.price-pill', '.price-badge', '.price-tag', '.canva-badge-price', '.chalk-badge-price',
            '.chalk-price',

            // Titles & Subtitles
            '.brand-title', '.brand-sub', '.canva-hero-title', '.canva-hero-sub',
            '.comic-hero-title', '.comic-hero-sub', '.card-category-title', '.card-category-tag',
            '.title-block', '.sandwich-name', '.pop-title', '.section-title', '.main-title', '.prefix',

            // Descriptions & Text
            '.item-title', '.item-desc', '.item-meta', '.item-badge-pill',
            '.banner-text', '.banner-highlight', '.card-footer-banner',

            // Cards & Containers
            '.ribbon-banner', '.card-footer', '.card-ribbon',
            '.menu-card', '.glass-acrylic-card', '.slate-card', '.dish-card', '.col-card', '.item-card', '.sandwich-card',
            '.menu-item-row',

            // Headings & Text
            'h1', 'h2', 'h3', 'h4', '.editable-text',

            // Images
            'img[src*="cutouts"]', 'img[src*="processed_images"]'
        ].join(', ');

        document.querySelectorAll(explicitSelectors).forEach(bindEditableElement);

        // Bind inner price numbers if not already bound
        document.querySelectorAll('.price-sand-num, .price-drk-num, .curr').forEach(bindEditableElement);

        // Dynamic scanner: find ANY element having price/tag/badge/kraft in class name
        document.querySelectorAll('*').forEach(el => {
            const cls = (el.className || '').toString().toLowerCase();
            if (cls.includes('price') || cls.includes('tag') || cls.includes('kraft') || cls.includes('badge')) {
                if (el.offsetWidth > 10 && el.offsetHeight > 10 && el.offsetWidth < 800 && el.offsetHeight < 600 && el.tagName !== 'BODY' && el.id !== 'stage' && el.id !== 'studio-price-modal') {
                    bindEditableElement(el);
                }
            }
        });

        loadLayout();
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initEditor);
    } else {
        initEditor();
    }
})();
