from django.conf.urls import include, url
from .views import portfolio

urlpatterns = [
    url(r'^', portfolio,  name='home'),
]