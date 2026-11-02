import subprocess
import json

chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# We can run headless chrome with a script or evaluate JS
test_html = """
<!DOCTYPE html>
<html>
<body>
<script>
async function run() {
    let res = await fetch('http://localhost:8000/api/menu_items');
    let data = await res.json();
    console.log("FETCHED_DATA:", JSON.stringify(data));
}
run();
</script>
</body>
</html>
"""
with open("c:/Users/pc/Desktop/menu/test_fetch.html", "w") as f:
    f.write(test_html)

print("Saved test_fetch.html")

