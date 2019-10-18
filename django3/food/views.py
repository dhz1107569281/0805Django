from django.shortcuts import render_to_response,render
from django.http import HttpResponse,JsonResponse
from food.models import *
# Create your views here.

# def test_re(request):
#     foods_type_id_list=foods_type.objects.all()
#     if request.method=='POST':
#         args=request.POST
#         name=args.get('name')
#         price=args.get('price')
#         description=args.get('description')
#         type_id=args.get('type_id')
#         picture=request.FILES.get('picture')
#
#         food=foods()
#         food.name=name
#         food.price=price
#         food.description=description
#         food.type_id=foods_type.objects.get(id=int(type_id))
#         food.picture=picture
#         # food.save()
#
#     return render(request,'test_re.html',locals())
def test_re(request):
    return render(request,'test_re.html',locals())
def find_food(request):
    food_name=request.GET.get('food_name')
    food_data=[]
    if food_name:
        food_list=foods.objects.filter(name__contains=food_name)
        for f in food_list:
            food_data.append({'name':f.name})
    return JsonResponse({'food_data':food_data})

def base(request):
    return render_to_response('base.html',locals())

#添加商品类型
def add_food_type(request):
    type_list=['经典牛排','意面/烩饭','风味披萨','甜品小食','酒水饮料','其他']
    for type in type_list:
        t=foods_type()
        t.label=type
        t.description='挺好吃的，就是有点费房子'
        # t.save()
    return HttpResponse('save')
#添加商品
def add_food(request):
    import random
    foods_list=['玉米海螺沟','芝士大虾','西冷牛排','草莓布丁杯','黑椒牛排','番茄烩意面','茶漱海鲜汤','芝士蛋糕卷']
    for food in foods_list:
        f=foods()
        f.name=food
        f.price=random.randint(19,79)
        f.picture='1.jpg'
        f.description='爱吃不吃'
        f.type_id=foods_type.objects.get(id=random.randint(1,6))
        # f.save()
    return HttpResponse('save')

def add_news(request):
    import random
    for new in range(10):
        new=news()
        new.title='贵族食代%s店开业'%random.choice(['北京','上海','广州','深圳','重庆','哈尔滨','浙江'])
        new.time='%s-%s-%s'%(
            random.randint(2000,2019),
            random.randint(1,12),
            random.randint(1,30)
        )
        new.description='欢迎光临'
        new.image='1.jpg'
        new.content='随便写写'
        new.type='新闻资讯'
        # new.save()
    return HttpResponse('save')

def add_shop(request):
    import random
    sp=shop()
    for i in range(10):
        sp.name ='贵族食代%s店开业'%random.choice(['北京','上海','广州','深圳','重庆','哈尔滨','浙江'])
        sp.picture ='1.jpg'
        sp.label = '法国菜,有包间,有车位,可刷卡,崇文区,地铁1号线,地铁2号线,地铁5号线,崇文门外大街,前门总医院,天坛,祈年殿,龙潭湖公园,北京体育馆,中央戏剧学院,崇文区儿童医院,新世界商场,北京站,新闻大厦,北京饭店,北京市政府,东交民巷,天安门,朋友聚会,家人就餐,谈情约会'
        sp.open_time = '上午9:00-13:30,下午5:30-10:30'
        sp.stop_car = '小车50大车100'
        sp.address = random.choice(['北京','上海','广州','深圳','重庆','哈尔滨','浙江'])
        # sp.save()
        for i in range(random.randint(6,8)):
            sp.foods_id.add(
                foods.objects.get(id=random.randint(1,8))
            )
            # sp.save()

    return HttpResponse('save')
def add_company(request):
    import random
    for i in range(10):
        com=company()
        com.name = '%s公司'%random.choice(['北京','上海','广州','深圳','重庆','哈尔滨','浙江'])
        com.picture = '1.jpg'
        com.phone = '010-484-2121-0038'
        com.fax = '09028'
        com.address = '%s'%random.choice(['北京','上海','广州','深圳','重庆','哈尔滨','浙江'])
        com.post_code = '129414'
        com.save()
    return HttpResponse('save')

def index(request):
    news_list=news.objects.all()
    foods_list=foods.objects.all()
    return render_to_response('index.html',locals())
def news_con(request,id):
    new=news.objects.filter(id=int(id))
    return render_to_response('news-con.html',locals())
def new(request):
    new_list=news.objects.all()
    return render_to_response('news.html',locals())
def about(request):
    company_list=company.objects.all()
    return render_to_response('about-us.html',locals())
def shops(request):
    shops_list=shop.objects.all()
    addre=request.GET.get('address')
    if addre:
        sp_list=shop.objects.filter(name__contains=addre)
    return render_to_response('shop.html',locals())

def shop_con(request,id):
    shop_info=shop.objects.get(id=int(id))
    shop_food=foods.objects.get(id=int(id))
    return render_to_response('shop-con.html',locals())
