import subprocess
import os

chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
out_img = r"C:\Users\pc\.gemini\antigravity\brain\b2a7b082-394c-4260-942a-782b3765aac5\verify_live_screen.png"

cmd = [
    chrome,
    "--headless=new",
    "--disable-gpu",
    "--window-size=1920,1080",
    f"--screenshot={out_img}",
    "http://127.0.0.1:8000/menu_model1_emirates.html"
]

res = subprocess.run(cmd, timeout=10)
print("Screenshot generated:", os.path.exists(out_img))
