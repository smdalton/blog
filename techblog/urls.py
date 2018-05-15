
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import include, url
from techblog import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.home_from_techblog, name="home_page"),

    # url(r'')
]