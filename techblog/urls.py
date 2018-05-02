
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import include, url
from techblog import views

urlpatterns = [
    url(r'^$', views.home_from_techblog, name="home_page"),
]