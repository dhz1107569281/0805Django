from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect,HttpResponse
from User.models import User
from Shop.models import *
from Shop.templates import *
from User.views import *
# Create your views here.

def register(request):
    # 注册功能
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")

        if vaild_email(email):#如果为真，说明邮箱存在，已经注册过了
            msg='邮箱已注册'
        else:
            password=set_password(password)#将邮箱加密，作为参数传入
            add_user(email=email, password=password)
            return HttpResponseRedirect('/Shop/login/')
    return render(request,'shop/register.html',locals())

def login(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')

        user=vaild_email(email)
        if user:#判断用户是否存在
            password=set_password(password)
            if password==user.password:#判断密码输入是否正确
                response=HttpResponseRedirect('/Shop/index/')
                response.set_cookie("email",email)
                request.session['email']=user.email
                return response
            else:
                msg='密码错误'
        else:
            msg='用户不存在'
    return render(request,'shop/login.html',locals())

def logout(request):
    response=HttpResponseRedirect('/Shop/login/')
    response.delete_cookie("email")
    request.session.clear()
    return response

def valid_login(fun):
    def inner(request,*args,**kwargs):
        cookie_email=request.COOKIES.get("email")
        session_email=request.session.get("email")
        if cookie_email and session_email and session_email==cookie_email:
            return fun(request,*args,**kwargs)
        else:
            return HttpResponseRedirect('/Shop/login/')
    return inner

@valid_login
def index(request):
    return render(request,'shop/index.html',locals())

def forgetpassword(request):
    return render(request,'shop/forgot-password.html',locals())

def reset_password(request):
    if request.method=='POST':
        email=request.POST.get('email')
        if email and vaild_email(email):
            hash_code=set_password(email)
            content="http://127.0.0.1:8000/Shop/change_password/?email=%s&token=%s"%(email,hash_code)
            get_mail(content,email)
    return HttpResponseRedirect("/Shop/forgetpassword/")

def change_password(request):
    if request.method == "POST":
        email = request.COOKIES.get("change_email")
        password = request.POST.get("password")

        e = User.objects.get(email=email)
        e.password = set_password(password)
        e.save()
        return HttpResponseRedirect("/Shop/login/")

    # 通过get请求获得了修改密码的用户和校验值
    email = request.GET.get("email")
    token = request.GET.get("token")
    # 进行再次校验
    now_token = set_password(email)
    # 当前提交人存在，并且token值正确
    if vaild_email(email) and now_token == token:
        # 返回修改密码页面
        response = render(request, "shop/change_password.html")
        # 设置cookie
        response.set_cookie("change_email", email)
        return response
    else:
        return HttpResponseRedirect("/Shop/forgetpassword/")

import smtplib
from email.mime.text import MIMEText
from Qshop.settings import MAIL_PASSWORD,MAIL_PORT,MAIL_SENDER,MAIL_SERVER
def sendemail(content,email):
    content="""
        点击链接进行修改密码
        <a href="%s">点击确认</a>
    """%(content)
    print(content)

    message=MIMEText(content,'html','utf-8')
    message["To"]=email
    message['From']=MAIL_SENDER
    message['Subject']='密码修改'
    try:
        smtp=smtplib.SMTP_SSL(MAIL_SERVER,MAIL_PORT)
        smtp.login(MAIL_SENDER,MAIL_PASSWORD)
        smtp.sendmail(MAIL_SENDER,[email],message.as_string())
        smtp.close()
    except Exception as e:
        return str(e)
    else:
        return

def base(request):

    return render(request,'shop/base.html',locals())

def profile(request):
    post_email=request.COOKIES.get('email')
    user=User.objects.get(email=post_email)
    return render(request,'shop/profile.html',locals())

def set_profile(request):
    post_email = request.COOKIES.get('email')
    user = User.objects.get(email=post_email)

    password=request.POST.get("password")
    if password:

        if vaild_email(post_email):
            user.password=set_password(password)
            user.save()
            response=HttpResponseRedirect('/Shop/login/')
            response.delete_cookie("email")
            return response
        else:
            print("账户不存在")

    elif not password:
        if request.method=='POST':
            arg=request.POST
            email=arg.get("email")
            username=arg.get("username")
            gender=arg.get("gender")
            age=arg.get("age")
            phone=arg.get("phone")
            address=arg.get("address")
            picture=request.FILES.get("picture")

            user.username=username
            user.email=email
            user.gender=gender
            user.age=age
            user.phone=phone
            user.address=address
            if picture:
                user.picture=picture
            user.save()
            return HttpResponseRedirect('/Shop/profile')

    return render(request, 'shop/set_profile.html', locals())

def add_goods(request):
    if request.method=="POST":
        arg=request.POST
        name=arg.get('name')
        price=arg.get('price')
        number=arg.get('number')
        production=arg.get('production')
        safe_date=arg.get('safe_date')
        description=arg.get('description')
        picture=request.FILES.get('picture')

        goods=Goods()
        goods.name=name
        goods.price=price
        goods.number=number
        goods.production=production
        goods.safe_date=safe_date
        goods.description=description
        goods.picture=picture
        goods.statue=1
        goods.save()
        return HttpResponseRedirect('/Shop/list_goods/')
    return render(request,'shop/add_goods.html',locals())

def list_goods(request):
    good_list=Goods.objects.all()
    return render(request, 'shop/list_goods.html', locals())

def set_statue(request,id):
    set_type = request.GET.get('set_type')
    goods=Goods.objects.get(id=int(id))
    if set_type == 'up':
        goods.statue=1
    elif set_type == 'down':
        goods.statue=0
    goods.save()
    return HttpResponseRedirect('/Shop/list_goods/')

def goods(request,id):
    goods_data=Goods.objects.get(id=id)
    return render(request,'shop/goods.html',locals())

def update_goods(request,id):
    goods_data = Goods.objects.get(id=id)
    if request.method=="POST":
        arg = request.POST
        name = arg.get('name')
        price = arg.get('price')
        number = arg.get('number')
        production = arg.get('production')
        safe_date = arg.get('safe_date')
        description = arg.get('description')
        picture = request.FILES.get('picture')

        goods_data.name = name
        goods_data.price = price
        goods_data.number = number
        goods_data.production = production.replace('年','-').replace('月','-').replace('日','')
        goods_data.safe_date = safe_date
        goods_data.description = description
        goods_data.picture = picture
        goods_data.statue=1
        goods_data.save()
        return HttpResponseRedirect('/Shop/list_goods/')

    return render(request, 'shop/update_goods.html', locals())

def Add_Update(request,id):
    html_type=request.GET.get("type")

    if id:
        goods=Goods.objects.get(id=id)

        if request.method == "POST":
            arg = request.POST
            name = arg.get('name')
            price = arg.get('price')
            number = arg.get('number')
            production = arg.get('production')
            safe_date = arg.get('safe_date')
            description = arg.get('description')
            picture = request.FILES.get('picture')

            goods.name = name
            goods.price = price
            goods.number = number
            goods.production = production
            goods.safe_date = safe_date
            goods.description = description
            goods.picture = picture
            goods.statue = 1
            goods.save()
            return HttpResponseRedirect('/Shop/list_goods/')
    else:
        if request.method == "POST":
            arg = request.POST
            name = arg.get('name')
            price = arg.get('price')
            number = arg.get('number')
            production = arg.get('production')
            safe_date = arg.get('safe_date')
            description = arg.get('description')
            picture = request.FILES.get('picture')

            goods = Goods()

            goods.name = name
            goods.price = price
            goods.number = number
            goods.production = production
            goods.safe_date = safe_date
            goods.description = description
            goods.picture = picture
            goods.statue = 1
            goods.save()
            return HttpResponseRedirect('/Shop/list_goods/')


        # if html_type=='1':
        #     goods=Goods()
        #
        #     goods.name = name
        #     goods.price = price
        #     goods.number = number
        #     goods.production = production
        #     goods.safe_date = safe_date
        #     goods.description = description
        #     goods.picture = picture
        #     goods.statue = 1
        #     goods.save()
        #     return HttpResponseRedirect('/Shop/list_goods/')
        # elif html_type == '2':
        #     goods=Goods.objects.get(id=id)
        #
        #     goods.name = name
        #     goods.price = price
        #     goods.number = number
        #     goods.production = production
        #     goods.safe_date = safe_date
        #     goods.description = description
        #     goods.picture = picture
        #     goods.statue = 1
        #     goods.save()
        #     return HttpResponseRedirect('/Shop/list_goods/')

    return render(request,'shop/Add_Update.html',locals())




from CeleryTask.tasks import sendMil

def get_mail(content,email):
    sendMil(content,email)
