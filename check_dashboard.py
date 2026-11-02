with open('dashboard.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if 'v-for="comp in' in line:
        for j in range(i, i+50):
            print(f'{j+1}: {lines[j].rstrip()}')
        break
