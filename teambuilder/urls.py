from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('teambuilder.apps.main.urls')),
    url(r'^', include('teambuilder.apps.user.urls')),
    url(r'^', include('teambuilder.apps.contact.urls')),
    url(r'^', include('teambuilder.apps.login.urls')),
    url(r'^', include('teambuilder.apps.lol.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
