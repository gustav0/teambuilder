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

