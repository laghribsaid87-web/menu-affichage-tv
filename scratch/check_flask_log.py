import json
import urllib.request

# Let's inspect the latest Flask server log to see if any POST /api/menu_items arrived!
with open(r"C:\Users\pc\.gemini\antigravity\brain\b2a7b082-394c-4260-942a-782b3765aac5\.system_generated\tasks\task-771.log", "r", encoding="utf-8", errors="ignore") as f:
    logs = f.readlines()

print("Last 30 lines of Flask server log:")
for l in logs[-30:]:
    print(l.strip())
