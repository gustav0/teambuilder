from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.http import condition

from teambuilder.apps.user.forms import registerForm
from teambuilder.apps.user.forms import summonerName
from teambuilder.apps.user.models import User


def register(request):
    form = registerForm(request.POST or None)
    if form.is_valid():
        form.save()
        user = authenticate(username=request.POST['email'], password=request.POST['password1'])
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/firststeps/')
            else:
                print 'user is not active'
        else:
            print 'the user is invalid'
    ctx = {'form':form}
    return render_to_response('user/register.html', ctx, context_instance=RequestContext(request))

@login_required
def firstSteps(request):
    if request.user.has_in_game_name():
        return redirect('/profile/')

    if request.method == 'POST':
        form = summonerName(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/profile/")
    else:
        form = summonerName(initial={'server': 'NA'})
    ctx = {'form':form}
    return render_to_response('user/firststeps.html', ctx, context_instance=RequestContext(request))

@login_required
def profile(request):
    return render_to_response('user/profile.html', context_instance=RequestContext(request))