import requests as _requests
import json
from django.shortcuts import render_to_response
from django.template import RequestContext
from teambuilder.apps.lol.models import Champion


def champions(request):
    title = 'TeamBuilder - Champions'
    champions = []
    for champ in Champion.objects.all():
        champions.append(champ)

    ctx = {'title':title, 'champions':champions}
    return render_to_response('lol/champions.html', ctx, context_instance=RequestContext(request))

def update_champions(request):
    requestJson = json.loads(_requests.get("https://prod.api.pvp.net/api/lol/lan/v1.1/champion?api_key=cc22a2c0-35d0-4bef-b178-deb4e925120a").text)

    for champion in requestJson['champions']:
        champ = Champion.objects.create(name=champion['name'], riot_id=champion['id'], difficulty_rank=champion['difficultyRank'], magic_rank=champion['magicRank'], attack_rank=champion['attackRank'], defense_rank=champion['defenseRank'], image="/static/img/champion/%s_Splash_0_e.jpg" % champion['name'])
        champ.save()
    return None

