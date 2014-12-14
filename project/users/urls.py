from django.conf.urls import patterns, include, url
from django.contrib import admin
from users.views import Index, Create, Welcome, Login, Logout, Games_history, High_scores

urlpatterns = patterns('',
    url(r'^$', Index.as_view() ),
    url(r'^create', Create.as_view() ),
    url(r'^login', Login.as_view() ),
    url(r'^logout', Logout.as_view() ),
    url(r'^(?P<user_id>[0-9]+)', Welcome.as_view() ),
    url(r'^(?P<user_id>[0-9]+)/history', Games_history.as_view() ),
    url(r'^highscores', High_scores.as_view() ),
)
