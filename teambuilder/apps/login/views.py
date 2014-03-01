from django.contrib.auth import authenticate, login as _login, logout as _logout
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.contrib.auth.tokens import default_token_generator
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.cache import never_cache
from django.contrib.auth.views import password_reset as _password_reset, password_reset_done as _password_reset_done,\
    password_reset_confirm as _password_reset_confirm, password_reset_complete as _password_reset_complete
from teambuilder.apps.login.forms import loginForm


def login(request):
    if not request.user.is_authenticated():
        form = loginForm(data=request.POST or None)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=email, password=password)
            if user is not None and user.is_active:
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

def password_reset(request, is_admin_site=False, post_reset_redirect=None, from_email=None, current_app=None,extra_context=None ):
    return _password_reset(request, is_admin_site, 'login/password_reset_form.html', 'login/password_reset_email.html',
        'login/password_reset_subject.txt',
        PasswordResetForm,
        default_token_generator,
        post_reset_redirect,
        from_email,
        current_app,
        extra_context)

def password_reset_done(request):
    return _password_reset_done(request, 'login/password_reset_done.html')

@sensitive_post_parameters()
@never_cache
def password_reset_confirm(request, uidb64=None, token=None, post_reset_redirect=None, current_app=None, extra_context=None):
    return _password_reset_confirm(request, uidb64, token, 'login/password_reset_confirm.html', default_token_generator,
        SetPasswordForm, post_reset_redirect, current_app, extra_context)

def password_reset_complete(request, current_app=None, extra_context=None):
    return _password_reset_complete(request,'login/password_reset_complete.html')