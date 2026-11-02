import subprocess
import sys
sys.stdout.reconfigure(encoding='utf-8')

chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
cmd = [
    chrome,
    "--headless=new",
    "--disable-gpu",
    "--dump-dom",
    "http://127.0.0.1:8000/test_selector.html"
]
res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=10)
out_text = res.stdout.decode('utf-8', errors='ignore')
for line in out_text.splitlines():
    if "title" in line.lower():
        print(line)
