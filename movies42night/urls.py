from django.conf.urls import url

from . import views

app_name = 'movies42night'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^movies/(?P<movie_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^movies/add/$', views.add, name='movies42night'),
    url(r'^movies/add/$', views.add, name='add'),
    url(r'^movies/$', views.list, name='movies42night'),
    url(r'^movies/add/$', views.list, name='list'),
]