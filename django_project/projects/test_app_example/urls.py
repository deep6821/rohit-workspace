from django.shortcuts import render
from django.conf.urls import url
from . import views

# Create your views here.
urlpatterns = [
    url(r'^index/$', views.index, name="index"),
    url(r'^register-user/$', views.register_user, name="register_user"),
    url(r'^get-user/$', views.get_user, name="get_user")
]
