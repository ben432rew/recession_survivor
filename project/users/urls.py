from django.conf.urls import patterns, include, url
from django.contrib import admin
from users.views import Index, Create, Welcome,Authenticate,Logout 

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bennys_first.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', Index.as_view() ),
    url(r'^create/$', Create.as_view() ),
    url(r'^welcome/$', Welcome.as_view() ),
    url(r'^login/$', Authenticate.as_view() ),
    url(r'^logout/$', Logout.as_view() ),
)
