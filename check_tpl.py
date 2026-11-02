with open('dashboard.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if 'v-if="comp.type' in line or '<div v-if="comp.type' in line or 'v-if="comp.type ===' in line:
        for j in range(i-2, i+30):
            print(f'{j+1}: {lines[j].strip()}')
        break
