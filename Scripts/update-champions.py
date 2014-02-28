import json, requests
from teambuilder.apps.lol.models import Champion
import sys

requestJson = json.loads(requests.get("https://prod.api.pvp.net/api/lol/lan/v1.1/champion?api_key=cc22a2c0-35d0-4bef-b178-deb4e925120a").text)

percent_per_item = 100.0000000000 / len(requestJson['champions'])
current_percent = 0

for champion in requestJson['champions']:
    champ = Champion.objects.create(name=champion['name'], riot_id=champion['id'], difficulty_rank=champion['difficultyRank'], magic_rank=champion['magicRank'], attack_rank=champion['attackRank'], defense_rank=champion['defenseRank'], free_play=champion['freeToPlay'], image="/static/img/champion/%s_Square_0.png" % champion['name'])
    current_percent += percent_per_item
    champ.save()
    sys.stdout.write('\r%.2f%%' % current_percent)
