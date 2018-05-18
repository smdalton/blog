
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import include, url
from techblog import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^post/$', views.techblog_post, name="post"),
    url(r'^$', views.home_from_techblog, name='blog_landing'),
    url(r'^post/$', views.techblog_post, name='tech_blog_post'),
    url(r'^signup/$', views.techblog_signup_page, name='tech_blog_signup'),
    url(r'^login/$', views.techblog_login_page, name='tech_blog_login')

    # url(r'')
]