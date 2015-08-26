from django.conf.urls import include, url
from .views import portfolio, resume, projects

urlpatterns = [
    url(r'^$', portfolio,  name='portfolio'),
    url(r'^resume/$', resume, name='resume'),
    url(r'^projects/$', projects, name='projects')
]