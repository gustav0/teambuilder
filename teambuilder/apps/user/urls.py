from django.conf.urls import patterns, url

urlpatterns = patterns('teambuilder.apps.user.views',
    url(r'profile/$', 'profile', name='profile'),
    url(r'profile/add/lol/$', 'profile_add_lol', name='profile_add_lol'),
    url(r'profile/add/personal/$', 'profile_add_personal', name='profile_add_personal'),

    url(r'account/$', 'account', name='account'),
    url(r'account/change/password/$', 'account_change_password', name='account_change_password'),

    url(r'register/$', 'register', name='register'),
)