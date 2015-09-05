from django.conf.urls import include, url
from django.contrib.auth.views import login, logout
from blog.views import home, makepost

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'login/$',
        login,
        name='Login'),
    url(r'logout/$',
        logout,
        {'next_page': 'blog:home'},
        name='Logout'),
    url(r'create-post/$', makepost, name='create-post'),
]