import subprocess

chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
cmd = [
    chrome,
    "--headless=new",
    "--disable-gpu",
    "--dump-dom",
    "file:///C:/Users/pc/Desktop/menu/dashboard_pro.html"
]
res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=10)
print("DOM snippet from file:///:", len(res.stdout))

