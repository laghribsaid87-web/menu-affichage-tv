with open('dashboard.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if 'v-for="(comp, cIdx) in' in line:
        for j in range(i-2, i+40):
            print(f'{j+1}: {lines[j].strip()}')
        break
