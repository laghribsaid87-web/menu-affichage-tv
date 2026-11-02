with open('dashboard.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if "comp.type === 'rawImage'" in line:
        for j in range(i-2, i+15):
            print(f'{j+1}: {lines[j].strip()}')
        break
