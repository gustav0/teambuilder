from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.shortcuts import render_to_response
from django.template import RequestContext
import requests
import json
from teambuilder.apps.lol.models import Champion
from teambuilder.settings import lol_api_key_1 as api_key

@cache_page(60 * 60)
def champions(request):
    champions = []
    for champ in Champion.objects.all():
        champions.append(champ)
    ctx = {'champions':champions}
    return render_to_response('lol/champions.html', ctx, context_instance=RequestContext(request))

#This method only saves the user, who has updated the region and the in_game_name values
def saveSummonerInfo(user):
    region = user.region
    requestAPI = cache.get('requestAPIByName')
    if requestAPI is None:
        requestAPI = requests.get('https://prod.api.pvp.net/api/lol/%s/v1.3/summoner/by-name/%s?api_key=%s' % (region.lower(), user.in_game_name.lower(), api_key))
        cache.set('requestAPIByName',requestAPI,600)
    jsonRequest = json.loads(requestAPI.text)
    user.lol_id = jsonRequest[str(user.in_game_name).lower()]['id']
    user.save()

# Returns a map with the profileIconId and summonerLevel
# Params id - User's lol_id
def getSummonerInfo(lol_id, region):
    requestAPI = cache.get('requestAPIById')
    if requestAPI is None:
        requestAPI = requests.get('https://prod.api.pvp.net/api/lol/%s/v1.3/summoner/%s?api_key=%s' % (region.lower(), str(lol_id), api_key))
        cache.set('requestAPIById',requestAPI,600)
    jsonRequest = json.loads(requestAPI.text)
    name = jsonRequest[str(lol_id)]['name']
    profileIconId = jsonRequest[str(lol_id)]['profileIconId']
    summonerLevel = jsonRequest[str(lol_id)]['summonerLevel']
    return {'name':name, 'profileIconId':profileIconId, 'summonerLevel':summonerLevel}

