import re

with open('tv_dynamic.html', 'r', encoding='utf-8') as f:
    content = f.read()

edit_script = """
        // ==========================================
        // VISUAL EDITOR MODE (if ?edit=1 in URL)
        // ==========================================
        const urlParams = new URLSearchParams(window.location.search);
        if(urlParams.has('edit')) {
            document.body.insertAdjacentHTML('beforeend', `
                <div class="fixed top-4 right-4 z-[9999] bg-white p-4 rounded-xl shadow-2xl border-4 border-red-500 text-black">
                    <h3 class="font-bold mb-2">Mode Édition Visuelle</h3>
                    <p class="text-sm text-gray-600 mb-2">Glissez (drag) le sandwich ou les frites pour les déplacer.</p>
                    <button id="save-visual-btn" class="bg-green-600 text-white px-4 py-2 rounded font-bold hover:bg-green-700 w-full">Sauvegarder</button>
                    <button onclick="window.location.href='tv_dynamic.html'" class="bg-gray-500 text-white px-4 py-2 rounded font-bold hover:bg-gray-600 w-full mt-2">Quitter (Play)</button>
                </div>
            `);

            function makeDraggable(el, settingX, settingY) {
                let isDragging = false;
                let startX, startY;
                let initialX = window.designSettings[settingX] || 0;
                let initialY = window.designSettings[settingY] || 0;

                el.style.cursor = 'grab';
                el.style.pointerEvents = 'auto'; // allow clicking

                el.addEventListener('mousedown', (e) => {
                    isDragging = true;
                    el.style.cursor = 'grabbing';
                    startX = e.clientX;
                    startY = e.clientY;
                    initialX = window.designSettings[settingX] || 0;
                    initialY = window.designSettings[settingY] || 0;
                    e.preventDefault();
                });

                window.addEventListener('mousemove', (e) => {
                    if(!isDragging) return;
                    const dx = e.clientX - startX;
                    const dy = e.clientY - startY;
                    window.designSettings[settingX] = initialX + dx;
                    window.designSettings[settingY] = initialY + dy;
                    
                    // Apply immediately
                    if(settingX.includes('sandwich')) {
                        const sS = (window.designSettings.spotlight_sandwich_scale || 110) / 100;
                        el.style.transform = `translate(${window.designSettings[settingX]}px, ${window.designSettings[settingY]}px) scale(${sS}) rotate(0deg)`;
                    } else {
                        const fS = (window.designSettings.spotlight_fries_scale || 100) / 100;
                        el.style.transform = `translate(${window.designSettings[settingX]}px, ${window.designSettings[settingY]}px) scale(${fS})`;
                    }
                });

                window.addEventListener('mouseup', () => {
                    if(isDragging) {
                        isDragging = false;
                        el.style.cursor = 'grab';
                    }
                });
            }

            setInterval(() => {
                const img = document.querySelector('.spotlight-img');
                const fries = document.querySelector('.absolute.top-\\[15\\%\\].right-\\[25\\%\\]');
                
                if(img && !img.dataset.draggable) {
                    img.dataset.draggable = "true";
                    makeDraggable(img, 'spotlight_sandwich_x', 'spotlight_sandwich_y');
                }
                if(fries && !fries.dataset.draggable) {
                    fries.dataset.draggable = "true";
                    makeDraggable(fries, 'spotlight_fries_x', 'spotlight_fries_y');
                }
            }, 1000);

            document.getElementById('save-visual-btn').addEventListener('click', async () => {
                const btn = document.getElementById('save-visual-btn');
                btn.innerText = "Sauvegarde...";
                
                try {
                    const res = await fetch('/api/dynamic_menu');
                    const fullData = await res.json();
                    
                    if(!fullData.settings) fullData.settings = {};
                    fullData.settings.spotlight_sandwich_x = window.designSettings.spotlight_sandwich_x;
                    fullData.settings.spotlight_sandwich_y = window.designSettings.spotlight_sandwich_y;
                    fullData.settings.spotlight_fries_x = window.designSettings.spotlight_fries_x;
                    fullData.settings.spotlight_fries_y = window.designSettings.spotlight_fries_y;
                    
                    await fetch('/api/dynamic_menu', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify(fullData)
                    });
                    
                    btn.innerText = "Sauvegardé !";
                    btn.className = "bg-blue-600 text-white px-4 py-2 rounded font-bold w-full";
                    setTimeout(() => {
                        btn.innerText = "Sauvegarder";
                        btn.className = "bg-green-600 text-white px-4 py-2 rounded font-bold hover:bg-green-700 w-full";
                    }, 2000);
                } catch(e) {
                    alert("Erreur de sauvegarde!");
                    btn.innerText = "Sauvegarder";
                }
            });
        }
"""

if 'VISUAL EDITOR MODE' not in content:
    content = content.replace('// End\n    </script>', edit_script + '\n        // End\n    </script>')
    with open('tv_dynamic.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Injected Visual Editor into tv_dynamic.html!")
else:
    print("Visual Editor already injected.")
