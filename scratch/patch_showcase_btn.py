with open("c:/Users/pc/Desktop/menu/menu_showcase.html", "r", encoding="utf-8") as f:
    c = f.read()

target = """        <div class="actions-group">
            <a id="btn-open-tv" href="/menu_model1_emirates.html" target="_blank" class="act-btn" style="background: #10b981;">
                📺 Ouvrir en Plein Écran TV
            </a>"""

replacement = """        <div class="actions-group">
            <a href="/dashboard_pro.html" target="_blank" class="act-btn" style="background: #ea580c; border: 1px solid rgba(255,255,255,0.2);">
                📱 Dashboard Prix
            </a>
            <a id="btn-open-tv" href="/menu_model1_emirates.html" target="_blank" class="act-btn" style="background: #10b981;">
                📺 Ouvrir en Plein Écran TV
            </a>"""

if target in c:
    c = c.replace(target, replacement, 1)
    with open("c:/Users/pc/Desktop/menu/menu_showcase.html", "w", encoding="utf-8") as f:
        f.write(c)
    print("SUCCESS")
else:
    target_crlf = target.replace("\n", "\r\n")
    replacement_crlf = replacement.replace("\n", "\r\n")
    if target_crlf in c:
        c = c.replace(target_crlf, replacement_crlf, 1)
        with open("c:/Users/pc/Desktop/menu/menu_showcase.html", "w", encoding="utf-8") as f:
            f.write(c)
        print("SUCCESS CRLF")
    else:
        print("NOT FOUND")

