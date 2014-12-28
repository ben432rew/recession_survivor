from django.conf.urls import patterns, include, url
from django.contrib import admin
from portfolio.views import *

urlpatterns = patterns('',
    url( r'^$', Index.as_view() ),
    url( r'^create$', Create.as_view() ),
    url( r'^(?P<slug>[\w\-]+)/edit$', Edit.as_view() ),
    url( r'^(?P<slug>[\w\-]+)/manage$', Manage.as_view() ),
    url( r'^(?P<slug>[\w\-]+)/manage/add$', Manage.as_view() ),
    url( r'^displayall$', Display_all.as_view() ),
    # url( r'(?P<slug>[\w\-]+$)', Display.as_view() ),
)
