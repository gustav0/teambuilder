from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from teambuilder.apps.user.forms import registerForm
from teambuilder.apps.user.forms import summonerName
from teambuilder.apps.user.models import User


def register(request):
    title = 'TeamBuilder - Register'
    form = registerForm(request.POST or None)
    if form.is_valid():
        form.save()
        new_user = authenticate(username=request.POST['email'], password=request.POST['password1'])
        login(request, new_user)
        return HttpResponseRedirect("/firststeps/")
    ctx = {'title':title, 'form':form}
    return render_to_response('user/register.html', ctx, context_instance=RequestContext(request))

@login_required
def firstSteps(request):
    title = 'TeamBuilder - First Steps'
    user = User.objects.get(pk=request.user.id)
    print user
    if request.method == 'post':
        form = summonerName(request.POST, instance=user)
        if form.is_valid():
            new_instance = form.save()
            return HttpResponseRedirect("/profile/")
    else:
        form = summonerName(instance=user)
    ctx = {'title':title, 'form':form}
    return render_to_response('user/firststeps.html', ctx, context_instance=RequestContext(request))

@login_required
def profile(request):
    title = 'TeamBuilder - User Profile'
    ctx = {'title':title}
    return render_to_response('user/profile.html', ctx, context_instance=RequestContext(request))