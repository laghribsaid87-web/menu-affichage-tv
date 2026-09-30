import os, requests, json
key = os.getenv("GROQ_API_KEY")
res = requests.get('https://api.groq.com/openai/v1/models', headers={'Authorization': f'Bearer {key}'}).json()
print([m['id'] for m in res['data'] if 'vision' in m['id']])
