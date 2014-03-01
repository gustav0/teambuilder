import requests as _requests
import json
from django.shortcuts import render_to_response
from django.template import RequestContext
from teambuilder.apps.lol.models import Champion
from teambuilder.settings import LOL_API as _api


def champions(request):
    champions = []
    for champ in Champion.objects.all():
        champions.append(champ)
    ctx = {'champions':champions}
    return render_to_response('lol/champions.html', ctx, context_instance=RequestContext(request))

def saveSummonerInfo(user):
    region = 'lan'
    requestJson = json.loads(_requests.get('https://prod.api.pvp.net/api/lol/%s/v1.3/summoner/by-name/%s?api_key=%s' % (user.in_game_name, _api)).text)
    user.lol_id = requestJson[user.in_game_name.lower()]['id']
    user.save()

def getSummonerInfo(id):
    region = 'lan'
    requestJson = json.loads(_requests.get('https://prod.api.pvp.net/api/lol/%s/v1.3/summoner/{%s}?api_key=%s' % (region, str(id), _api)).text)

    print requestJson

