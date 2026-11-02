import re

sample_price = '''<div style="background:#111827; border:3px double #fcd535; border-radius:8px; padding:6px 14px; display:flex; align-items:center; gap:12px; box-shadow:0 8px 20px rgba(0,0,0,0.7), inset 0 0 10px rgba(0,0,0,0.8); font-family:'Oswald',sans-serif;">
    <div style="display:flex; flex-direction:column; align-items:center;">
        <span style="font-size:11px; color:#94a3b8; font-weight:700; letter-spacing:1px;">SEUL</span>
        <span style="font-size:24px; color:#fff; font-weight:900; line-height:1;">29<span style="font-size:13px; color:#fcd535; font-weight:900; margin-left:2px;">DH</span></span>
    </div>
    <div style="width:1px; height:28px; background:rgba(255,255,255,0.2);"></div>
    <div style="display:flex; flex-direction:column; align-items:center;">
        <span style="font-size:11px; color:#94a3b8; font-weight:700; letter-spacing:1px;">MENU</span>
        <span style="font-size:24px; color:#fff; font-weight:900; line-height:1;">39<span style="font-size:13px; color:#fcd535; font-weight:900; margin-left:2px;">DH</span></span>
    </div>
</div>'''

sample_title = '''<div style="display:flex; align-items:baseline; gap:8px;">
    <span style="font-family:'Bebas Neue',sans-serif; font-size:30px; color:#1e293b; letter-spacing:2px; font-style:italic;">LE</span>
    <span style="font-family:'Titan One',cursive; font-size:42px; color:#d91c1c; text-shadow:0 1px 0 #fff, 0 2px 0 #8b0000, 0 3px 0 #8b0000, 0 4px 0 #8b0000, 0 8px 15px rgba(0,0,0,0.5); letter-spacing:1px; line-height:1;">COMPLET</span>
</div>'''

sample_ribbon = '''<div style="background:linear-gradient(to right, rgba(0,0,0,0.82), rgba(20,20,20,0.88)); color:#ffffff; font-family:'Montserrat',sans-serif; font-size:11px; font-weight:800; letter-spacing:1px; padding:4px 14px; border-radius:4px; box-shadow:0 4px 10px rgba(0,0,0,0.6); border-left:3px solid #ffaa00; white-space:nowrap;">
    THON • TORTILLA • FROMAGE • CHARCUTERIE • SAUCES
</div>'''

def test_price(c):
    m_seul = re.search(r'SEUL[\s\S]*?>(\+?\d+)<span', c, re.I)
    m_menu = re.search(r'MENU[\s\S]*?>(\d+)<span', c, re.I)
    print("Price Seul:", m_seul.group(1) if m_seul else None)
    print("Price Menu:", m_menu.group(1) if m_menu else None)
    
    # replace
    c_new = re.sub(r'(SEUL[\s\S]*?>)(\+?\d+)(<span)', r'\g<1>33\g<3>', c, flags=re.I)
    c_new = re.sub(r'(MENU[\s\S]*?>)(\d+)(<span)', r'\g<1>43\g<3>', c_new, flags=re.I)
    m_seul2 = re.search(r'SEUL[\s\S]*?>(\+?\d+)<span', c_new, re.I)
    m_menu2 = re.search(r'MENU[\s\S]*?>(\d+)<span', c_new, re.I)
    print("Updated Seul:", m_seul2.group(1) if m_seul2 else None)
    print("Updated Menu:", m_menu2.group(1) if m_menu2 else None)

def test_title(c):
    m = re.search(r'font-size:42px[\s\S]*?>([^<]+)</span>', c, re.I)
    print("Title:", m.group(1).strip() if m else None)
    c_new = re.sub(r'(font-size:42px[\s\S]*?>)([^<]+)(</span>)', r'\g<1>ROYALE\g<3>', c, flags=re.I)
    m2 = re.search(r'font-size:42px[\s\S]*?>([^<]+)</span>', c_new, re.I)
    print("Updated Title:", m2.group(1).strip() if m2 else None)

def test_ribbon(c):
    m = re.search(r'white-space:nowrap;[^>]*>\s*([\s\S]*?)\s*</div>', c, re.I)
    print("Ribbon:", m.group(1).strip() if m else None)
    c_new = re.sub(r'(white-space:nowrap;[^>]*>\s*)([\s\S]*?)(\s*</div>)', r'\g<1>NOUVEAUX INGREDIENTS\g<3>', c, flags=re.I)
    m2 = re.search(r'white-space:nowrap;[^>]*>\s*([\s\S]*?)\s*</div>', c_new, re.I)
    print("Updated Ribbon:", m2.group(1).strip() if m2 else None)

test_price(sample_price)
test_title(sample_title)
test_ribbon(sample_ribbon)

