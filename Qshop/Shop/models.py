from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Goods(models.Model):
    name=models.CharField(max_length=32)
    price=models.FloatField()
    number=models.IntegerField()
    production=models.DateTimeField()
    safe_date=models.CharField(max_length=32)
    picture=models.ImageField(upload_to='',default='shop/img/haski.jpg')
    description=RichTextField()

    statue=models.IntegerField()#状态0 下架 1上架