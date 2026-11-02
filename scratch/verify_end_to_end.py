import urllib.request
import json
import subprocess
import sys
sys.stdout.reconfigure(encoding='utf-8')

# 1. Update Tortilla Royale to 34 via API
with open("c:/Users/pc/Desktop/menu/menu_items.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for it in data['items']:
    if it['id'] == 'tortilla_royale':
        it['price_sandwich'] = '34'
        break

req = urllib.request.Request(
    "http://127.0.0.1:8000/api/menu_items",
    data=json.dumps(data).encode('utf-8'),
    headers={"Content-Type": "application/json"}
)
urllib.request.urlopen(req)
print("Updated Tortilla Royale to 34 DH via POST /api/menu_items")

# 2. Check DOM of menu_model1_emirates.html
chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
cmd = [
    chrome,
    "--headless=new",
    "--disable-gpu",
    "--virtual-time-budget=3000",
    "--dump-dom",
    "http://127.0.0.1:8000/menu_model1_emirates.html"
]
res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=10)
dom = res.stdout.decode('utf-8', errors='ignore')

found_34 = "34" in dom
print("Was 34 found in model 1 DOM?:", found_34)

# Reset back to 30
for it in data['items']:
    if it['id'] == 'tortilla_royale':
        it['price_sandwich'] = '30'
        break

req2 = urllib.request.Request(
    "http://127.0.0.1:8000/api/menu_items",
    data=json.dumps(data).encode('utf-8'),
    headers={"Content-Type": "application/json"}
)
urllib.request.urlopen(req2)
print("Reset back to 30 DH")
