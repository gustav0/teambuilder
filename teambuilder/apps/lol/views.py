import requests
import json

r = requests.get("https://prod.api.pvp.net/api/lol/lan/v1.1/champion?freeToPlay=true&api_key=cc22a2c0-35d0-4bef-b178-deb4e925120a")
r.text

print json.loads(r.text)

print json.dumps(r.text)