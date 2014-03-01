from django.conf.urls import patterns, url

urlpatterns = patterns('teambuilder.apps.login.views',
    url(r'^login/$', 'login', name='login'),
    url(r'^logout$', 'logout', name='logout'),
    url(r'^user/password/reset/$', 'password_reset', {'post_reset_redirect' : '/user/password/reset/done/'}, name="password_reset"),
    url(r'^user/password/reset/done/$', 'password_reset_done'),
    url(r'^user/password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', 'password_reset_confirm', {'post_reset_redirect' : '/user/password/done/'}, name='password_reset_confirm'),
    url(r'^user/password/done/$', 'password_reset_complete'),
)