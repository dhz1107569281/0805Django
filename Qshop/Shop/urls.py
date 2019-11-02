from django.urls import path,re_path
from Shop.views import *

urlpatterns = [
    path('register/',register),
    path('base/',base),
    path('login/',login),
    path('logout/',logout),
    path('index/',index),
    path('profile/',profile),
    path('set_profile/',set_profile),
    path('forgetpassword/',forgetpassword),
    path('reset_password/',reset_password),
    path('change_password/',change_password),
    path('add_goods/',add_goods),
    path('list_goods/',list_goods),
    re_path(r'set_statue/(?P<id>\d+)/',set_statue),
    re_path(r'goods/(?P<id>\d+)/',goods),
    re_path(r'update_goods/(?P<id>\d+)/',update_goods),
    re_path(r'Add_Update/(?P<id>\d*)',Add_Update),

    path('Goods/',GoodsView.as_view()),
    path('vue_list_goods/',vue_list_goods),
]
urlpatterns +=[
    path('get_mail/',get_mail)
]