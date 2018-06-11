from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import include, url
from techblog import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.techblog_home, name='blog_landing'),
    url(r'^markdown_test/', views.markdown_test),
    url(r'^signup/$', views.techblog_signup, name='tech_blog_signup'),
    url(r'^posts/$', views.posts, name='tech_blog_posts'),
    url(r'^login/$', views.techblog_login, name='tech_blog_login')
]