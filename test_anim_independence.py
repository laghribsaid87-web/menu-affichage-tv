# -*- coding: utf-8 -*-
import subprocess

html = """<!DOCTYPE html>
<html>
<head>
<style>
#box {
    width: 100px; height: 100px; background: red;
    transform: translateX(50px) !important;
    animation: floatAnim 2s infinite alternate;
}
@keyframes floatAnim {
    0% { translate: 0px 0px; }
    100% { translate: 0px -20px; }
}
</style>
</head>
<body>
<div id="box"></div>
<script>
const el = document.getElementById('box');
const style = window.getComputedStyle(el);
document.body.innerHTML += '<p id="res">TRANSFORM: ' + style.transform + ' | TRANSLATE: ' + style.translate + '</p>';
</script>
</body>
</html>"""

with open(r'c:\Users\pc\Desktop\menu\test_translate.html', 'w', encoding='utf-8') as f:
    f.write(html)

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
cmd = [chrome_path, "--headless=new", "--dump-dom", r"c:\Users\pc\Desktop\menu\test_translate.html"]
res = subprocess.run(cmd, capture_output=True, text=True)
print("Result in DOM:")
for line in res.stdout.splitlines():
    if "TRANSFORM:" in line:
        print(line)

