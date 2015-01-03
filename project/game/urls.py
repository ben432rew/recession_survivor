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
    url(r'^round/portfolio/$', PortfolioView.as_view(), name='portfolio' ),
    url(r'^round/portfolio/buy/$', BuyView.as_view(), name='buy' ),
    url(r'^round/portfolio/buy/checkout/$', CheckoutView.as_view(), name='checkout' ),
    url(r'^find/$', UnfinishedGames.as_view(), name='unfinished' ),
)