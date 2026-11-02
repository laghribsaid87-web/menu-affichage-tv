import sys

with open("c:/Users/pc/Desktop/menu/server.py", "r", encoding="utf-8") as f:
    content = f.read()

target = "@app.route('/api/save_emirates_config'"

git_push_route = """@app.route('/api/publish_to_tv', methods=['POST'])
def publish_to_tv():
    try:
        cmd = 'git add . && git commit -m "Mise a jour automatique depuis Dashboard" && git push'
        proc = subprocess.run(cmd, shell=True, cwd=MENU_DIR, capture_output=True, text=True, timeout=30)
        return jsonify({
            "success": True, 
            "stdout": proc.stdout,
            "stderr": proc.stderr
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/save_emirates_config'"""

if target in content and "/api/publish_to_tv" not in content:
    content = content.replace(target, git_push_route, 1)
    with open("c:/Users/pc/Desktop/menu/server.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("SUCCESS: Added /api/publish_to_tv")
else:
    print("Already added or target not found")

