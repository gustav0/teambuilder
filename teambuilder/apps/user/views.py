from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from teambuilder.apps.user.forms import registerForm
from teambuilder.apps.user.forms import summonerName
from teambuilder.apps.lol.views import saveSummonerInfo, getSummonerInfo

def register(request):
    if not request.user.is_authenticated():
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
    else:
        return render(request, 'user/error.html')


@login_required
def firstSteps(request):
    if request.method == 'POST':
        form = summonerName(request.POST, instance=request.user)
        if form.is_valid():
            saveSummonerInfo(form.save())
            return HttpResponseRedirect("/profile/")
    else:
        form = summonerName(initial={'server': 'NA'})
    ctx = {'form':form}
    return render_to_response('user/firststeps.html', ctx, context_instance=RequestContext(request))

@login_required
def profile(request):
    if request.user.lol_id is not None:
        information = getSummonerInfo(request.user.lol_id)
    else:
        information = None
    return render_to_response('user/profile.html', context_instance=RequestContext(request))