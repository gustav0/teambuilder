from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.cache import cache
from django.forms.forms import NON_FIELD_ERRORS
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext

from teambuilder.apps.user.forms import registerForm
from teambuilder.apps.user.forms import summonerInformation, personalInformation
from teambuilder.apps.lol.views import saveSummonerInfo, getSummonerInfo
from django.contrib.auth.views import password_change as _password_change
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm

def register(request):
    if not request.user.is_authenticated():
        form = registerForm(request.POST or None)
        if form.is_valid():
            form.save()
            user = authenticate(username=request.POST['email'], password=request.POST['password1'])
            if user is not None and user.is_active:
                login(request, user)
                return redirect('/profile/add/lol/')
        ctx = {'form': form}
        return render_to_response('user/register.html', ctx, context_instance=RequestContext(request))
    else:
        return render(request, 'user/error.html')


@user_passes_test(lambda u: u.lol_id is None, '/profile/')
@login_required
def profile_add_lol(request):
    message = 'We need your League of Legends\' summoner name.'
    if request.method == 'POST':
        form = summonerInformation(request.POST, instance=request.user)
        if form.is_valid():
            result = saveSummonerInfo(form.save())
            if result:
                cache.delete('summoner_information')
                return HttpResponseRedirect("/profile/")
            else:
                form._errors[NON_FIELD_ERRORS] = form.error_class(['That\'s not a valid user.'])
    else:
        form = summonerInformation(initial={'server': 'NA'})
        message = 'We need your League of Legends\' summoner name.'
    ctx = {'form': form, 'message': message}
    return render_to_response('user/profile_add.html', ctx, context_instance=RequestContext(request))


@login_required
def profile_add_personal(request):
    if request.method == 'POST':
        form = personalInformation(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            cache.delete('profile')
            return HttpResponseRedirect("/profile/")
    else:
        form = personalInformation()
    ctx = {'form': form}
    return render_to_response('user/profile_add.html', ctx, context_instance=RequestContext(request))


@login_required
def profile(request):
    if request.user.lol_id is not None:
        information = cache.get('summoner_information')
        if information is None:
            information = getSummonerInfo(request.user.lol_id, request.user.region)
            cache.add('summoner_information', information, 600)
    else:
        information = None
    ctx = {'summoner': information}
    return render_to_response('user/profile.html', ctx, context_instance=RequestContext(request))


@login_required
def account(request):
    setPasswordForm = SetPasswordForm(request.user)
    changePasswordForm = PasswordChangeForm(setPasswordForm)
    ctx = {'PasswordChangeForm':changePasswordForm}
    return render_to_response('user/account.html', ctx, context_instance=RequestContext(request))

@login_required
def account_change_password(request):
    return _password_change(request, 'user/account.html', 'account', PasswordChangeForm)
