import sys

with open("c:/Users/pc/Desktop/menu/server.py", "r", encoding="utf-8") as f:
    content = f.read()

target = "return jsonify({\"success\": True})\n    except Exception as e:\n        return jsonify({\"error\": str(e)}), 500\n\n\n\n@app.route('/api/save_emirates_config'"

replacement = """return jsonify({"success": True})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/menu_items', methods=['GET'])
def get_menu_items():
    try:
        if not os.path.exists(MENU_ITEMS_FILE):
            return jsonify({"items": [], "global_settings": {}})
        with open(MENU_ITEMS_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/menu_items', methods=['POST'])
def save_menu_items():
    try:
        import datetime
        data = request.json
        if "global_settings" not in data:
            data["global_settings"] = {}
        data["global_settings"]["updated_at"] = datetime.datetime.now().isoformat()
        with open(MENU_ITEMS_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return jsonify({"success": True, "updated_at": data["global_settings"]["updated_at"]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/save_emirates_config'"""

if target in content:
    content = content.replace(target, replacement, 1)
    with open("c:/Users/pc/Desktop/menu/server.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("SUCCESS")
else:
    # try with CRLF
    target_crlf = target.replace("\n", "\r\n")
    replacement_crlf = replacement.replace("\n", "\r\n")
    if target_crlf in content:
        content = content.replace(target_crlf, replacement_crlf, 1)
        with open("c:/Users/pc/Desktop/menu/server.py", "w", encoding="utf-8") as f:
            f.write(content)
        print("SUCCESS CRLF")
    else:
        print("TARGET NOT FOUND")

