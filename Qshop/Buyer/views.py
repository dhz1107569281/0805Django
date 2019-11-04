from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect,HttpRequest
from Shop.models import GoodsType,Goods
from User.models import User
from Buyer.models import BuyCar
from Shop.views import vaild_email,set_password
# Create your views here.


def login(request):
    referer=request.GET.get("referer")
    if not referer:
        referer = request.META.get("HTTP_REFERER")  # 获取上一个页面来源
    if request.method=="POST":
        email=request.POST.get("email")#获取form表单提交来的数据
        password=request.POST.get("password")
        user=vaild_email(email)#验证用户是否存在
        if user:
            db_password=user.password
            request_password=set_password(password)
            if db_password==request_password:#将post来的密码加密后和数据库密码比较
                if request.POST.get("referer"):
                    referer=request.POST.get("referer")
                if referer in ('http://127.0.0.1:8000/Buyer/index/',"http://127.0.0.1:8000/Buyer/register/"):
                    referer='/Buyer/index/'
                response=HttpResponseRedirect(referer)
                response.set_cookie("email",email)
                response.set_cookie("user_id",user.id)
                request.session["email"]=user.email
                return response
            else:
                error="密码错误"
        else:
            error='用户不存在'
    return render(request,'buyer/login.html',locals())

def index(request):
    # message='hello world'
    # all_data = GoodsType.objects.all()
    four_goods = GoodsType.objects.getfour(1)
    email=request.COOKIES.get("email")
    type_list=GoodsType.objects.all()
    # result=[{t.name:t.goods_set.all(),"picture":t.picture} for t in type_list]

    return render(request,'buyer/index.html',locals())

from django.core.paginator import Paginator
def goods_list(request):
    email = request.COOKIES.get("email")
    id=request.GET.get("id")
    goodslist=Goods.objects.all()
    if id:
        goods_type=GoodsType.objects.get(id=int(id))
        goodslist=goods_type.goods_set.all()
        goods_obj=Paginator(goods_list,2)
        # goods_data=goods_obj.page(int(1))
    return render(request,'buyer/goods_list.html',locals())

def goods(request,id):
    email = request.COOKIES.get("email")
    goodsdata=Goods.objects.get(id=int(id))
    return render(request,'buyer/goods.html',locals())


# def cart(request):#方法一
#     cookie_email=request.COOKIES.get("email")
#     session_email=request.session.get("email")
#     if cookie_email and session_email and cookie_email==session_email:
#         return render(request,"buyer/cart.html")
#
#     return HttpResponseRedirect('/Buyer/login/?referer=/Buyer/cart/')
def login_valid(fun):
    def inner(request,*args,**kwargs):
        referer = request.GET.get("referer")
        cookie_user = request.COOKIES.get("email")
        session_user = request.session.get("email")
        if cookie_user and session_user and cookie_user==session_user:
            return fun(request,*args,**kwargs)
        else:
            login_url='/Buyer/login/'
            if referer:
                login_url='/Buyer/login/?referer=%s'%referer
            return HttpResponseRedirect(login_url)
    return inner

@login_valid
def cart(request):#方法二
    email = request.COOKIES.get("email")
    return  render(request,'buyer/cart.html',locals())

def register(request):
    if request.method=="POST":
        arg=request.POST
        email=arg.get("email")
        username=arg.get("username")
        password=arg.get("password")
        repassword=arg.get("repassword")

        user=User()
        user.email=email
        user.username=username
        if password==repassword:
            user.password=set_password(password)
        else:
            return HttpResponseRedirect('/Buyer/register/')
        user.save()
        return HttpResponseRedirect('/Buyer/login/')
    return  render(request,'buyer/register.html',locals())

def logout(request):
    response=HttpResponseRedirect('/Buyer/login')
    response.delete_cookie("email")
    response.delete_cookie("user_id")
    del request.session["email"]
    return response

def place_order(request):
    return render(request,'buyer/place_order.html')

import time
from Buyer.pay import pay
def get_pay(request):
    order_number=str(time.time()).replace(".","")
    order_price="340"
    url=pay(order_number,order_price)
    return HttpResponseRedirect(url)

def user_center_info(request):
    email=request.COOKIES.get("email")
    user_info=User.objects.get(email=email)
    return render(request,'buyer/user_center_info.html',locals())

from django.http import JsonResponse
def add_car(request):
    result={
        "statue":"error",
        "data":""
    }
    if request.method=="POST":
        user = request.COOKIES.get("email")
        goods_id = request.POST.get("goods_id")
        number = request.POST.get("number",1)

        try:
            goods=Goods.objects.get(id=goods_id)
        except Exception as e:
            result["data"]=str(e)
        else:
            car = BuyCar()
            car.car_user=user
            car.goods_name=goods.name
            car.goods_picture=goods.picture
            car.goods_price=goods.price
            car.goods_number=number
            car.goods_total=number*goods.price
            car.goods_store=goods.goods_store_id
            car.save()
            result["statue"]="success"
            result["data"]="加入购物车成功"
        return JsonResponse(result)