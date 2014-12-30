from django.conf.urls import patterns, include, url
from django.contrib import admin
from game.views import *

urlpatterns = patterns('',
    url( r'^$', Index.as_view(), name='index' ),
    url(r'^create/', CreateView.as_view(), name='create' ),
    url(r'^round/', RoundView.as_view(), name='round' ),
)