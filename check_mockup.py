with open('dashboard.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if 'id="mockup-anim' in line:
        for j in range(i-5, i+40):
            print(f'{j+1}: {lines[j].strip()}')
        break
