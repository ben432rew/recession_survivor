from django.conf.urls import patterns, include, url
from django.contrib import admin
from ui.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url( r'^$', Index.as_view(), name='index' ),
    # url( r'^blog$', include( blog.urls ) ),
    # url( r'^admin/', include( admin.site.urls ) ),
)
