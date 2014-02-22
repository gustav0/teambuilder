from django.conf.urls import patterns, url

urlpatterns = patterns('teambuilder.apps.contact.views',
    url(r'contact/$', 'contact', name='contact'),
    url(r'thanks/$', 'thanks', name='thanks'),
)