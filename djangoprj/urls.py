"""djangoprj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.shortcuts import render
from django.contrib import admin
from app001.views import login
from django.http import HttpResponse
from app001.views import customized404


# handler500 = home
# handler400 = home
handler404 = customized404

def index(request):
    """直接访问网址时的网站"""

    return HttpResponse("欢迎光临小窝")


urlpatterns = [
    url(r'^app001', include("app001.urls")),
    url(r'^login', login, name='login'),
    url(r'^$', index, name="index")
]
