from django.conf.urls import patterns, include, url
from users.views import *

urlpatterns = patterns('',
    url(r'^$', Index.as_view() ),
    url(r'^signup', Signup.as_view() ),
    url(r'^login', Login.as_view() ),
    url(r'^logout', Logout.as_view() ),
    url(r'^profile', Profile.as_view() ),
    url(r'^changepassword', ChangePass.as_view() ),
)
