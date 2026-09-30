with open('dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()
content = content.replace('{{ comp.content }}', '<div v-html="comp.content || \'&nbsp;\'"></div>', 2)
with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(content)
