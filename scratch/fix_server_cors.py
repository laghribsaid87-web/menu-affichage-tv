import sys

with open("c:/Users/pc/Desktop/menu/server.py", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update add_no_cache_headers to include full CORS
old_headers = """@app.after_request
def add_no_cache_headers(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response"""

new_headers = """@app.after_request
def add_no_cache_headers(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS, PUT, DELETE'
    return response"""

content = content.replace(old_headers, new_headers, 1)

# 2. Update index() to serve dashboard_pro.html
old_index = """@app.route('/')
def index():
    return send_from_directory(MENU_DIR, 'dashboard.html')"""

new_index = """@app.route('/')
def index():
    return send_from_directory(MENU_DIR, 'dashboard_pro.html')"""

content = content.replace(old_index, new_index, 1)

with open("c:/Users/pc/Desktop/menu/server.py", "w", encoding="utf-8") as f:
    f.write(content)

print("SUCCESS: Updated server.py CORS and index route.")

