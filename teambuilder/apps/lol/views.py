import requests as _requests
import json
from django.shortcuts import render_to_response
from django.template import RequestContext


def champions(request):
    title = 'TeamBuilder - Champions'
    requestLeague = _requests.get("https://prod.api.pvp.net/api/lol/lan/v1.1/champion?freeToPlay=true&api_key=cc22a2c0-35d0-4bef-b178-deb4e925120a")
    dataJson = json.loads(requestLeague.text)
    champions = []
    for champion in dataJson['champions']:
        champions.append(champion['name'])
        #var1 = "Champion name: %s" % (champion['name'])
    ctx = {'title':title, 'champions':champions}
    return render_to_response('lol/champions.html', ctx, context_instance=RequestContext(request))