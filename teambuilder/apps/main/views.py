from django.shortcuts import render_to_response
from django.template import RequestContext
from teambuilder.apps.login.forms import loginForm

def index(request):
    if request.user.is_authenticated():
        form = None
    else:
        form = loginForm()
    ctx = {'form':form}
    return render_to_response('main/index.html', ctx, context_instance=RequestContext(request))