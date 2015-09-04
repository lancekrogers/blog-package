from django.conf.urls import include, url
from django.contrib.auth.views import login, logout
from blog.views import home

urlpatterns = [
    url(r'login/$', login, name='Login'),
    url(r'logout/$', logout, name='Logout'),
    url(r'', home, name='home'),

]