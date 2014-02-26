from django.conf.urls import patterns, url

urlpatterns = patterns('teambuilder.apps.login.views',
    url(r'^login/$', 'login', name='login'),
    url(r'^logout$', 'logout', name='logout'),
)
