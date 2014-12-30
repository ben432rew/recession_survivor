from django.conf.urls import patterns, include, url
from django.contrib import admin
from game.views import *

urlpatterns = patterns('',
    url( r'^', Index.as_view() ),
    url(r'^create/', CreateView.as_view() ),
    # url(r'^history/', Games_history.as_view() ),
    # url(r'^round/', Round.as_view() ),
    # url(r'^endgame/', Endgame.as_view() ),
)