from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^/gameState$', views.game_state),
    url(r'^/(?P<name>[a-zA-Z]+)$', views.index),
    url(r'^/prep/(?P<name>[a-zA-Z]+)$', views.prep_game),
    url(r'^/how_to_play$', views.how_to_play),
    url(r'^/fight$', views.fight),
    url(r'^/character_info$', views.character_info),
    url(r'^/update/(?P<name>[a-zA-Z]+)$', views.processMove),
    url(r'^/update/(?P<name>[a-zA-Z]+)/rest', views.processRest),
    url(r'^/endTurn$', views.endTurn)
]