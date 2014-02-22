from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    title = 'TeamBuilder'
    ctx = {'title':title}
    return render_to_response('main/index.html', ctx, context_instance=RequestContext(request))