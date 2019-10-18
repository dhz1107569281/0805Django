"""django3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,re_path
from food.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', base),
    path('add_food_type/', add_food_type),
    path('add_food/', add_food),
    path('add_news/', add_news),
    path('add_shop/',add_shop),
    path('add_company/',add_company),
    path('index/',index),
    re_path(r'news_con/(?P<id>\d+)',news_con),
    path('news/',new),
    path('about-us/',about),
    path('shop/',shops),
    re_path(r'shop_con/(?P<id>\d+)',shop_con),

]
urlpatterns += [
    path('test_re/',test_re),
    path('find_food/',find_food),
]
