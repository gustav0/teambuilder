from django.conf.urls import patterns, url

urlpatterns = patterns('teambuilder.apps.user.views',
    url(r'profile/$', 'profile', name='profile'),
    url(r'register/$', 'register', name='register'),
    url(r'firststeps/$', 'firstSteps', name='firststeps'),
)