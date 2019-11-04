from django.urls import path,re_path
from Buyer.views import *

urlpatterns = [
    path('index/',index),
    path('goods_list/',goods_list),
    re_path(r'goods/(?P<id>\d+)',goods),
    path('cart/',cart),
    path('place_order/',place_order),
    path('get_pay/',get_pay),
    path('add_car/',add_car),
]

urlpatterns +=[
    path('login/',login),
    path('register/',register),
    path('logout/',logout),
    path('user_center_info/',user_center_info),
]