from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^processIndex$', views.processIndex),
    url(r'^setup/(?P<name>[a-zA-Z]+)$', views.setup),
    url(r'^reset$', views.reset)
]