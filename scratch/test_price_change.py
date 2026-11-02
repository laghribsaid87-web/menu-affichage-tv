import urllib.request
import json
import subprocess
import sys
sys.stdout.reconfigure(encoding='utf-8')

# 1. Read current menu_items.json
with open("c:/Users/pc/Desktop/menu/menu_items.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Change Complet price to 99 for a test
data['items'][0]['price_sandwich'] = "99"
with open("c:/Users/pc/Desktop/menu/menu_items.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Saved Complet price as 99 DH in menu_items.json")

# 2. Dump DOM of menu_model1_emirates.html via Chrome headless
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

# Check if 99DH is in dom
found_99 = "99" in dom
print("Was 99 found in DOM?:", found_99)

# Reset back to 29
data['items'][0]['price_sandwich'] = "29"
with open("c:/Users/pc/Desktop/menu/menu_items.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
