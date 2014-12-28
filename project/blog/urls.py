from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog.views import *

urlpatterns = patterns('',

    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', IndexView.as_view()),
    url(r'^create$', Create.as_view() ),
    url(r'^post/(?P<slug>[\w\-]+$)',BlogDisplayView.as_view())
)
