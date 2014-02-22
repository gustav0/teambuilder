from django.conf.urls import patterns, url

urlpatterns = patterns('teambuilder.apps.main.views',
    url(r'^$', 'index', name='index'),
    url(r'^contact/$', 'contact', name='contact'),
)
