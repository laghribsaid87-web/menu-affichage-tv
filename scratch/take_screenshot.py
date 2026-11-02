import subprocess
import os

chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
out_img = r"C:\Users\pc\.gemini\antigravity\brain\b2a7b082-394c-4260-942a-782b3765aac5\screen_dashboard_pro.png"

cmd = [
    chrome,
    "--headless=new",
    "--disable-gpu",
    "--window-size=1280,900",
    f"--screenshot={out_img}",
    "http://127.0.0.1:8000/dashboard_pro.html"
]

res = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
print("Returncode:", res.returncode)
print("File exists:", os.path.exists(out_img), "Size:", os.path.getsize(out_img) if os.path.exists(out_img) else 0)

