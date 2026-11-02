with open('tv_dynamic.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re

# We will replace the entire edit_script part.
# The edit script is enclosed between "// VISUAL EDITOR MODE" and "// End"
new_edit_script = """
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

            let isDragging = false;
            let currentTarget = null;
            let startX, startY;
            let initialX = 0, initialY = 0;
            let settingX, settingY;

            document.addEventListener('mousedown', (e) => {
                const target = e.target;
                let found = null;
                
                // Check if we clicked the big sandwich
                if(target.classList.contains('spotlight-img')) {
                    found = target;
                    settingX = 'spotlight_sandwich_x';
                    settingY = 'spotlight_sandwich_y';
                }
                // Check if we clicked the fries (the img inside the div)
                else if(target.alt === 'Frites') {
                    // Go up to the container
                    if (target.parentElement.classList.contains('absolute') && target.parentElement.style.transform) {
                        found = target.parentElement; // move the container
                        settingX = 'spotlight_fries_x';
                        settingY = 'spotlight_fries_y';
                    }
                }

                if(found) {
                    isDragging = true;
                    currentTarget = found;
                    startX = e.clientX;
                    startY = e.clientY;
                    initialX = window.designSettings[settingX] || 0;
                    initialY = window.designSettings[settingY] || 0;
                    e.preventDefault();
                }
            });

            document.addEventListener('mousemove', (e) => {
                if(!isDragging || !currentTarget) return;
                const dx = e.clientX - startX;
                const dy = e.clientY - startY;
                window.designSettings[settingX] = initialX + dx;
                window.designSettings[settingY] = initialY + dy;
                
                if(settingX.includes('sandwich')) {
                    const sS = (window.designSettings.spotlight_sandwich_scale || 110) / 100;
                    currentTarget.style.transform = `translate(${window.designSettings[settingX]}px, ${window.designSettings[settingY]}px) scale(${sS}) rotate(0deg)`;
                } else {
                    const fS = (window.designSettings.spotlight_fries_scale || 100) / 100;
                    currentTarget.style.transform = `translate(${window.designSettings[settingX]}px, ${window.designSettings[settingY]}px) scale(${fS})`;
                }
            });

            document.addEventListener('mouseup', () => {
                if(isDragging) {
                    isDragging = false;
                    currentTarget = null;
                }
            });
            
            // Add hover cursor styles globally using CSS
            const style = document.createElement('style');
            style.innerHTML = `
                .spotlight-img:hover { cursor: grab !important; outline: 3px dashed red; outline-offset: 5px; }
                img[alt="Frites"]:hover { cursor: grab !important; outline: 3px dashed red; outline-offset: 5px; }
            `;
            document.head.appendChild(style);

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

content = re.sub(r'// ==========================================\n        // VISUAL EDITOR MODE.*?// End', new_edit_script + '\n        // End', content, flags=re.DOTALL)

with open('tv_dynamic.html', 'w', encoding='utf-8') as f:
    f.write(content)
