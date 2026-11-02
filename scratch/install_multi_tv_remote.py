import sys

models = ['menu_model1_emirates.html', 'menu_model2_urban.html', 'menu_model3_vibrant.html']

script_to_add = """
    <!-- ========================================== -->
    <!-- 📺 MULTI-TV REMOTE ASSIGNMENT (1, 2, 0)   -->
    <!-- ========================================== -->
    <script>
    (function() {
        function showTvToast(msg) {
            let t = document.getElementById('tv-remote-toast');
            if (!t) {
                t = document.createElement('div');
                t.id = 'tv-remote-toast';
                t.style.cssText = 'position:fixed; top:30px; left:50%; transform:translateX(-50%); background:rgba(0,0,0,0.85); color:#fff; font-family:Montserrat,sans-serif; font-size:20px; font-weight:800; padding:12px 28px; border-radius:30px; border:2px solid #ffaa00; box-shadow:0 10px 30px rgba(0,0,0,0.7); z-index:999999; pointer-events:none; transition:opacity 0.4s;';
                document.body.appendChild(t);
            }
            t.innerText = msg;
            t.style.opacity = '1';
            clearTimeout(t._timer);
            t._timer = setTimeout(() => { t.style.opacity = '0'; }, 3000);
        }

        window.addEventListener('keydown', (e) => {
            if (e.target && (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA')) return;

            if (e.key === '1') {
                localStorage.setItem('TV_LOCKED_SCREEN', '1');
                if (typeof setScreenMode === 'function') setScreenMode('screen-1');
                showTvToast('📺 TV Verrouillée : Écran 1 (Bocadillos Tradition)');
            } else if (e.key === '2') {
                localStorage.setItem('TV_LOCKED_SCREEN', '2');
                if (typeof setScreenMode === 'function') setScreenMode('screen-2');
                showTvToast('📺 TV Verrouillée : Écran 2 (Sandwiches Chauds)');
            } else if (e.key === '0' || e.key === 'a' || e.key === 'A') {
                localStorage.removeItem('TV_LOCKED_SCREEN');
                if (typeof setScreenMode === 'function') setScreenMode('auto');
                showTvToast('🔄 TV en Boucle Automatique (15s)');
            }
        });

        // Auto-restore on startup
        window.addEventListener('DOMContentLoaded', () => {
            const locked = localStorage.getItem('TV_LOCKED_SCREEN');
            if (locked === '1' && typeof setScreenMode === 'function') {
                setScreenMode('screen-1');
            } else if (locked === '2' && typeof setScreenMode === 'function') {
                setScreenMode('screen-2');
            }
        });
    })();
    </script>
"""

for m in models:
    path = f"c:/Users/pc/Desktop/menu/{m}"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "MULTI-TV REMOTE ASSIGNMENT" not in content:
        content = content.replace("</body>", script_to_add + "\n</body>")
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Installed remote TV assignment in", m)
    else:
        print("Already installed in", m)

