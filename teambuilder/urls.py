from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('teambuilder.apps.main.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
