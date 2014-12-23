from django.conf.urls import patterns, include, url
from django.contrib import admin
from portfolio.views import Find_stock_by_name, Display_all, Display_owned, Buy_stock, Sell_shares

urlpatterns = patterns('',
    url(r'^displayall', Display_all.as_view() ),
    url(r'^displayowned', Display_owned.as_view() ),
    url(r'^buystock', Buy_stock.as_view() ),
    url(r'^sellshares', Sell_shares.as_view() ),
)
