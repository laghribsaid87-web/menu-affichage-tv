import urllib.request
import json

# Test what happens when dashboard_pro sends a POST
test_payload = {
    "items": [
        {
            "id": "complet",
            "screen": 1,
            "title": "COMPLET",
            "title_prefix": "LE",
            "price_sandwich": "31",
            "price_drink": "+7",
            "is_available": True
        }
    ],
    "global_settings": {
        "active_model": 1
    }
}

req = urllib.request.Request(
    "http://localhost:8000/api/menu_items",
    data=json.dumps(test_payload).encode('utf-8'),
    headers={"Content-Type": "application/json"}
)

try:
    resp = urllib.request.urlopen(req)
    print("Direct POST response:", resp.getcode(), resp.read().decode())
except Exception as e:
    print("Direct POST failed:", e)

