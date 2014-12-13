from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^game/', include('game.urls', namespace = 'game')),
    url(r'^users/', include('users.urls', namespace = 'users')),
    # url(r'^portfolio/', include('portfolio.urls', namespace = 'portfolio')),
)
