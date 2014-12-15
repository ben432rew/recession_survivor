from django.conf.urls import patterns, include, url
from django.contrib import admin
from game.views import Round, Endgame, Index, Welcome, Games_history, High_scores

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bennys_first.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url( r'^$', Index.as_view() ),
    url(r'^history/', Games_history.as_view() ),
    url(r'^highscores/', High_scores.as_view() ),    
    url(r'^round/', Round.as_view() ),
    url(r'^endgame/', Endgame.as_view() ),
)