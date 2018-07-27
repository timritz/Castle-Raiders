from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^/(?P<name>[a-zA-Z]+)$', views.index),
    url(r'^/prep/(?P<name>[a-zA-Z]+)$', views.prep_game),
    url(r'^/how_to_play$', views.how_to_play),
    url(r'^/character_info$', views.character_info),
    url(r'^/update/(?P<name>[a-zA-Z]+)$', views.updateGame),
    url(r'^/update/(?P<name>[a-zA-Z]+)/fight$', views.processFight),
    url(r'^/update/(?P<name>[a-zA-Z]+)/rest', views.processRest)
]