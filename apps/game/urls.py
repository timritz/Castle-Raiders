from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^/(?P<name>[a-zA-Z]+)$', views.index),
    url(r'^/prep/(?P<name>[a-zA-Z]+)$', views.prep_game)
]