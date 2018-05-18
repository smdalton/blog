"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from techblog import views as tech_blog_views
from . import views

urlpatterns = [
                  url(r'^$', views.landing, name="home_page"),
                  url(r'^admin/', admin.site.urls),
                  url(r'^about/$', views.about, name='about_page'),
                  url(r'^projects/$', views.projects, name='projects'),
                  url(r'^techblog/', include('techblog.urls')),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
