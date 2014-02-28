from django.contrib.auth import authenticate, login as _login, logout as _logout
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from teambuilder.apps.login.forms import loginForm



def login(request):
    if not request.user.is_authenticated():
        form = loginForm(data=request.POST or None)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=email, password=password)

            print email + ' ' + password

            if user and user.is_active:
                _login(request, user)
                return HttpResponseRedirect('/profile/')
            else:
                form.non_field_errors.append('The provided information isn\'t valid.')
        else:
            print form.errors
        ctx = {'form':form}
        return render_to_response('login/login.html', ctx, context_instance=RequestContext(request))
    else:
        return render(request, 'user/error.html')

def logout(request):
    _logout(request)
    return HttpResponseRedirect('/')