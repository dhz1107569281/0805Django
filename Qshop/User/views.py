from Shop.views import *
from Shop.templates import *
import  hashlib
from django.http import HttpResponseRedirect
from django.shortcuts import render,render_to_response
# Create your views here.

def set_password(password):
    md5=hashlib.md5()
    md5.update(password.encode())
    ret=md5.hexdigest()
    return ret

def add_user(**kwargs):
    # 添加用户
    if "email" in kwargs and "username" not in kwargs:#如果传过来的参数没有username，说明注册页面没有将用户名传回，即没有设置
        kwargs["username"]=kwargs["email"]#如果没有用户名，将邮件作为默认用户名
    user = User.objects.create(**kwargs)
    return user

def vaild_email(email):
    try:
        user=User.objects.get(email=email)
    except Exception as e:
        return False
    else:
        return user