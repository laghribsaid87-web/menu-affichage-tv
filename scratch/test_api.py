import urllib.request
import json

# 1. Fetch current items
req = urllib.request.urlopen("http://localhost:8000/api/menu_items")
data = json.loads(req.read().decode('utf-8'))
print("Total items:", len(data['items']))
print("First item:", data['items'][0]['title'], "Price:", data['items'][0]['price_sandwich'])

# 2. Test saving (POST)
data['items'][0]['price_sandwich'] = "29" # keep 29
post_req = urllib.request.Request(
    "http://localhost:8000/api/menu_items",
    data=json.dumps(data).encode('utf-8'),
    headers={'Content-Type': 'application/json'}
)
resp = urllib.request.urlopen(post_req)
print("POST Response:", resp.read().decode('utf-8'))

