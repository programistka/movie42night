from django.conf import settings
from django.conf.urls import include, url

from . import views

app_name = 'movies42night'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^movies/(?P<movie_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^movies/add/$', views.add, name='movies42night'),
    url(r'^movies/add/$', views.add, name='add_proposition'),
    url(r'^movies/all$', views.list_all, name='list_all'),
    url(r'^movies/accepted$', views.list_accepted, name='list_accepted'),
    url(r'^movies/rejected', views.list_rejected, name='list_rejected'),
    url(r'^movies/new$', views.list_new, name='list_new'),
    url(r'^movies/private', views.list_private, name='list_private'),
    url(r'^movies/process_movie/(?P<pk>[0-9]+)', views.process_movie, name='process_movie'),
]
