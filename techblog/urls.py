from django.conf.urls import url
from techblog import views


urlpatterns = [
    url(r'^$', views.techblog_home, name='blog_landing'),
    url(r'^markdown_test/', views.markdown_test),
    url(r'^signup/$', views.techblog_signup, name='tech_blog_signup'),
    url(r'^login/$', views.techblog_login, name='tech_blog_login'),
    url(r'^view-post/(?P<post_id>\w{0,50})/$', views.display_post, name='display_post'),
]
