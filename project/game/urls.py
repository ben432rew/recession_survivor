from django.conf.urls import patterns, include, url
from django.contrib import admin
from game.views import *

urlpatterns = patterns('',
    url( r'^$', CreateGame.as_view(), name='creategame' ),
    url( r'^(?P<game_id>[\d]+)/start$', Start.as_view(), name='start' ),
    url( r'^(?P<game_id>[\d]+)/manage$', Manage.as_view(), name='manage' ),
    url( r'^(?P<game_id>[\d]+)/manage/add$', Manage_add.as_view(), name='manage_add' ),
    url( r'^(?P<game_id>[\d]+)/manage/remove$', Manage_remove.as_view(), name='manage_remove' ),
    url( r'^(?P<game_id>[\d]+)/round$', RoundView.as_view(), name='round' ),
    url(r'^round/stats/$', StatsView.as_view(), name='stats' ),
    url(r'^find/$', UnfinishedGames.as_view(), name='unfinished' ),
    url(r'^endgame/$', EndGame.as_view(), name='endgame' ),
