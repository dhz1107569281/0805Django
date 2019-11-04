from django.db import models

# Create your models here.

class BuyCar(models.Model):

    car_user=models.CharField(max_length=32)
    goods_name= models.CharField(max_length=32)
    goods_picture=models.ImageField(upload_to="")
    goods_price=models.FloatField()
    goods_number=models.IntegerField()
    goods_total=models.FloatField()
    goods_store=models.IntegerField()
