import re
with open('dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()
matches = re.finditer(r'<div id="mockup-anim', content)
for m in matches:
    idx = m.start()
    lines = content[:idx].count('\n')
    for j in range(lines-2, lines+30):
        print(f'{j+1}: {content.splitlines()[j]}')
    break
