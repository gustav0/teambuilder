from django.conf.urls import patterns, url

urlpatterns = patterns('teambuilder.apps.login.views',
    url(r'^login/$', 'login', name='login'),
    url(r'^logout$', 'logout', name='logout'),
    url(r'^account/reset_password$', 'password_reset', {'post_reset_redirect' : '/account/reset_done'}, name="password_reset"),
    url(r'^account/reset_done$', 'password_reset_done'),
    url(r'^account/reset_password/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', 'password_reset_confirm', {'post_reset_redirect' : '/account/password_done'}, name='password_reset_confirm'),
    url(r'^account/password_done$', 'password_reset_complete'),
)