from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^game/', include('game.urls', namespace = 'game')),
    url(r'^portfolio/', include('portfolio.urls', namespace = 'portfolio')),    
    url(r'^users/', include('users.urls', namespace = 'users')),
    url(r'^/$', include('users.urls', namespace = 'users')),
)
