from django.conf.urls import include, url
from .views import portfolio, home

urlpatterns = [
    url(r'^', portfolio,  name='home'),
    url(r'^home/$', home)
]