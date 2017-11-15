"""djangoTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from hz import views
from django.contrib.auth import views as auth_views
from django.contrib.auth import settings


urlpatterns = [
    url(r'^accounts/login/', auth_views.login, name='login',
        kwargs={'template_name': 'hz/login.html', 'next_page':'^$' }),
    url(r'^accounts/logout/', auth_views.logout, name='logout',
        kwargs={'next_page': settings.LOGIN_URL, }),
    url(r'^$', views.rest_post, name='rest_post'),
    url(r'^admin/', admin.site.urls),
]
