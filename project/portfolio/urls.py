from django.conf.urls import patterns, include, url
from django.contrib import admin
from portfolio.views import *

urlpatterns = patterns('',
    url( r'^create$', Create.as_view() ),
    url( r'^edit/(?P<slug>[\w\-]+$)', Edit.as_view() ),
    url(r'^displayall$', Display_all.as_view() ),
    url(r'^displayowned$', Display_owned.as_view() ),
    url(r'^buystock$', Buy_stock.as_view() ),
    url(r'^sellshares$', Sell_shares.as_view() ),
)
