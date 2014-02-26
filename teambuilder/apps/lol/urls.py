from django.conf.urls import patterns, url

urlpatterns = patterns('teambuilder.apps.lol.views',
    url(r'champions/$', 'champions', name='champions'),
)