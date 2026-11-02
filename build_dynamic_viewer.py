import os

source_path = r'c:\Users\pc\Desktop\menu\viewer_engine.html'
with open(source_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update title and fonts in <head>
old_head = '''    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Oswald:wght@700;900&family=Inter:wght@400;700;900&display=swap" rel="stylesheet">'''

new_head = '''    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Montserrat:ital,wght@0,400;0,700;0,800;0,900;1,800&family=Titan+One&family=Oswald:wght@700;900&family=Inter:wght@400;700;900&display=swap" rel="stylesheet">
    <title>Menu TV Live 1080p - Mon Bocadillo Tanger</title>'''

content = content.replace(old_head, new_head)

# 2. Add Emirates 3D and floating UI styles
ui_css = '''
        /* Emirates 3D and Title styles */
        .title-3d {
            font-family: 'Titan One', cursive;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .ui-controls {
            position: fixed;
            bottom: 20px;
            right: 20px;
            z-index: 99999;
            display: flex;
            gap: 10px;
            background: rgba(15, 23, 42, 0.88);
            padding: 8px 16px;
            border-radius: 40px;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            box-shadow: 0 10px 25px rgba(0,0,0,0.5);
            opacity: 0;
            transition: opacity 0.3s;
        }
        .ui-controls:hover, .ui-controls.visible {
            opacity: 1;
        }
        .btn-ctl {
            background: #334155;
            color: #fff;
            border: none;
            padding: 7px 16px;
            border-radius: 20px;
            font-size: 13px;
            font-weight: 800;
            cursor: pointer;
            transition: all 0.2s;
            font-family: 'Montserrat', sans-serif;
            display: flex;
            align-items: center;
            gap: 6px;
        }
        .btn-ctl:hover, .btn-ctl.active {
            background: #e11d48;
        }
'''

content = content.replace('</style>', ui_css + '\n    </style>')

# 3. Fix promos safe check in loadData
old_promos = '''            if (menuData.promos) {
                document.getElementById('promo-video').src = menuData.promos.video;
                document.getElementById('promo-image').src = menuData.promos.image;
            }'''

new_promos = '''            if (menuData.promos) {
                if (menuData.promos.video && document.getElementById('promo-video')) document.getElementById('promo-video').src = menuData.promos.video;
                if (menuData.promos.image && document.getElementById('promo-image')) document.getElementById('promo-image').src = menuData.promos.image;
            }'''

content = content.replace(old_promos, new_promos)

# 4. Safe check in startProAnimationLoop
old_loop_promos = '''            // Promos
            if(menuData.promos.video) {'''

new_loop_promos = '''            // Promos
            if(menuData.promos && menuData.promos.video) {'''

content = content.replace(old_loop_promos, new_loop_promos)

old_loop_img = '''            if(menuData.promos.image) {'''
new_loop_img = '''            if(menuData.promos && menuData.promos.image) {'''
content = content.replace(old_loop_img, new_loop_img)

# 5. Add controls and live sync polling before </body>
controls_html = '''
    <!-- Floating TV Controls -->
    <div class="ui-controls" id="tv-controls">
        <button id="btn-auto" class="btn-ctl active" onclick="setScreenMode('auto')">Auto-Boucle (15s)</button>
        <button id="btn-s1" class="btn-ctl" onclick="setScreenMode('screen-1')">TV 1: Bocadillos</button>
        <button id="btn-s2" class="btn-ctl" onclick="setScreenMode('screen-2')">TV 2: Sandwiches</button>
        <button id="btn-sound" class="btn-ctl" onclick="toggleSound()">🔊 Son</button>
        <button id="btn-fs" class="btn-ctl" onclick="toggleFullScreen()">⛶ Plein Écran</button>
        <a href="/dashboard.html" class="btn-ctl" style="background:#2563eb; text-decoration:none;">✏️ Modifier dans CMS</a>
    </div>

    <!-- Audio Player -->
    <audio id="bg-audio" loop preload="auto">
        <source src="music_menu.aac" type="audio/aac">
        <source src="ref_audio.m4a" type="audio/mp4">
    </audio>

    <script>
        // Auto-show/hide controls on mouse move
        let ctlTimeout = null;
        const ctlBar = document.getElementById('tv-controls');
        function showCtl() {
            if (!ctlBar) return;
            ctlBar.classList.add('visible');
            if (ctlTimeout) clearTimeout(ctlTimeout);
            ctlTimeout = setTimeout(() => ctlBar.classList.remove('visible'), 3000);
        }
        window.addEventListener('mousemove', showCtl);
        window.addEventListener('touchstart', showCtl);
        showCtl();

        // Screen mode controls
        let screenMode = 'auto';
        function setScreenMode(mode) {
            screenMode = mode;
            document.querySelectorAll('.ui-controls .btn-ctl').forEach(b => b.classList.remove('active'));
            const views = Array.from(document.querySelectorAll('.dyn-view'));
            
            if (mode === 'auto') {
                document.getElementById('btn-auto').classList.add('active');
                if (masterTimeline) masterTimeline.play();
            } else if (mode === 'screen-1' && views[0]) {
                document.getElementById('btn-s1').classList.add('active');
                if (masterTimeline) {
                    masterTimeline.pause();
                    gsap.set(views, { autoAlpha: 0 });
                    gsap.set(views[0], { autoAlpha: 1 });
                }
            } else if (mode === 'screen-2' && views[1]) {
                document.getElementById('btn-s2').classList.add('active');
                if (masterTimeline) {
                    masterTimeline.pause();
                    gsap.set(views, { autoAlpha: 0 });
                    gsap.set(views[1], { autoAlpha: 1 });
                }
            }
        }

        // Fullscreen
        function toggleFullScreen() {
            if (!document.fullscreenElement) {
                document.documentElement.requestFullscreen().catch(e => {});
            } else {
                if (document.exitFullscreen) document.exitFullscreen();
            }
        }

        // Sound
        let isAudioPlaying = false;
        function toggleSound() {
            const a = document.getElementById('bg-audio');
            const btn = document.getElementById('btn-sound');
            if (!a) return;
            if (isAudioPlaying) {
                a.pause();
                isAudioPlaying = false;
                btn.innerHTML = '🔇 Son';
                btn.classList.remove('active');
            } else {
                a.play().then(() => {
                    isAudioPlaying = true;
                    btn.innerHTML = '🔊 Son Actif';
                    btn.classList.add('active');
                }).catch(e => console.log('Audio error:', e));
            }
        }

        // Live Auto-Refresh when user clicks 'Sauvegarder' in Dashboard!
        let initialDataHash = null;
        setInterval(async () => {
            try {
                const urlParams = new URLSearchParams(window.location.search);
                const targetProject = urlParams.get('project') || 'default';
                const targetTv = urlParams.get('tv') || '1';
                const res = await fetch(`/api/menu/${targetProject}/${targetTv}?t=${Date.now()}`);
                if (res.ok) {
                    const text = await res.text();
                    if (initialDataHash === null) {
                        initialDataHash = text;
                    } else if (text !== initialDataHash) {
                        console.log('Detected menu update from CMS! Refreshing TV...');
                        location.reload();
                    }
                }
            } catch(e) {}
        }, 2000);
    </script>
'''

content = content.replace('</body>', controls_html + '\n</body>')

with open(r'c:\Users\pc\Desktop\menu\viewer.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('SUCCESSFULLY CREATED DYNAMIC viewer.html!')

