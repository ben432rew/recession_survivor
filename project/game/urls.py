from django.conf.urls import patterns, include, url
from django.contrib import admin
from game.views import *

urlpatterns = patterns('',
    url( r'^$', CreateGame.as_view(), name='creategame' ),
    url(r'^round/$', RoundView.as_view(), name='round' ),
    url(r'^round/stats/$', StatsView.as_view(), name='stats' ),
    url(r'^round/portfolio/$', PortfolioView.as_view(), name='portfolio' ),
    url(r'^round/portfolio/buy/$', BuyView.as_view(), name='buy' ),
    url(r'^round/portfolio/buy/checkout/$', CheckoutView.as_view(), name='checkout' ),
    url(r'^find/$', UnfinishedGames.as_view(), name='unfinished' ),
)