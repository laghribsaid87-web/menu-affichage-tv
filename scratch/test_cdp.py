import subprocess
import time
import urllib.request
import json

chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# Start chrome with remote debugging
proc = subprocess.Popen([
    chrome,
    "--headless=new",
    "--remote-debugging-port=9222",
    "http://127.0.0.1:8000/dashboard_pro.html"
])

time.sleep(2)

try:
    # Query targets
    targets = json.loads(urllib.request.urlopen("http://127.0.0.1:9222/json").read().decode())
    print("Chrome targets:", [t['url'] for t in targets])
finally:
    proc.kill()

