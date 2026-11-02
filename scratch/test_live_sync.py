import urllib.request
import json
import time
import subprocess
import os

# 1. Update Tortilla Royale to 33 DH
req = urllib.request.urlopen("http://localhost:8000/api/menu_items")
data = json.loads(req.read().decode('utf-8'))
for item in data['items']:
    if item['id'] == 'tortilla_royale':
        item['price_sandwich'] = '33'
        break

post_req = urllib.request.Request(
    "http://localhost:8000/api/menu_items",
    data=json.dumps(data).encode('utf-8'),
    headers={'Content-Type': 'application/json'}
)
urllib.request.urlopen(post_req)
print("Updated Tortilla Royale to 33 DH via API")

# 2. Open headless chrome with a delay so JS runs sync
chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
out_img = r"C:\Users\pc\.gemini\antigravity\brain\b2a7b082-394c-4260-942a-782b3765aac5\test_sync_screen.png"

cmd = [
    chrome,
    "--headless=new",
    "--disable-gpu",
    "--window-size=1920,1080",
    "--virtual-time-budget=4000",
    f"--screenshot={out_img}",
    "http://127.0.0.1:8000/menu_model1_emirates.html"
]
subprocess.run(cmd, timeout=15)

# Reset back to 30 DH
for item in data['items']:
    if item['id'] == 'tortilla_royale':
        item['price_sandwich'] = '30'
        break
post_req2 = urllib.request.Request(
    "http://localhost:8000/api/menu_items",
    data=json.dumps(data).encode('utf-8'),
    headers={'Content-Type': 'application/json'}
)
urllib.request.urlopen(post_req2)
print("Reset back to 30 DH. Screenshot generated:", os.path.exists(out_img))

