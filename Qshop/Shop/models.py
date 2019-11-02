from django.db import models
from ckeditor.fields import RichTextField
from User.models import *
# Create your models here.

class GoodsTypeManager(models.Manager):
    def getfour(self,id):
        return self.get(id=id).goods_set.all()[:4]


class GoodsType(models.Model):
    name=models.CharField(max_length=32)
    picture=models.ImageField(upload_to='shop/img',default='shop/img/1.jpg')
    objects = GoodsTypeManager()

class Goods(models.Model):
    name=models.CharField(max_length=32)
    price=models.FloatField()
    number=models.IntegerField()
    production=models.DateTimeField()
    safe_date=models.CharField(max_length=32)
    picture=models.ImageField(upload_to='',default='shop/img/haski.jpg')
    description=RichTextField()

    statue=models.IntegerField()#状态0 下架 1上架
    goods_type=models.ForeignKey(to=GoodsType,on_delete=models.CASCADE)
    goods_store=models.ForeignKey(to=User,on_delete=models.CASCADE)