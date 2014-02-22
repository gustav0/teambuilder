from django.shortcuts import render_to_response
from django.template import RequestContext
from teambuilder.apps.user.forms import registerForm

def profile(request):
    titulo = 'TeamBuilder'
    ctx = {'titulo':titulo}
    return render_to_response('user/profile.html', ctx, context_instance=RequestContext(request))

def register(request):
    titulo = 'TeamBuilder - Register'
    form = registerForm(request.POST or None)
    if form.is_valid():
        form.save()
    ctx = {'titulo':titulo, 'form':form}
    return render_to_response('user/register.html', ctx, context_instance=RequestContext(request))