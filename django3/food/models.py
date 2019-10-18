from django.db import models

class foods_type(models.Model):
    label=models.CharField(max_length=32)
    description=models.TextField()

class foods(models.Model):
    name=models.CharField(max_length=32)
    price=models.FloatField()
    picture=models.ImageField(upload_to='img')
    description=models.TextField()
    type_id=models.ForeignKey(to=foods_type,on_delete=models.CASCADE)

class shop(models.Model):
    name=models.CharField(max_length=32)
    picture=models.ImageField(upload_to='img')
    foods_id=models.ManyToManyField(to=foods)
    label=models.TextField()
    open_time=models.CharField(max_length=32)
    stop_car=models.CharField(max_length=32)
    address=models.TextField()

class company(models.Model):
    name=models.CharField(max_length=32)
    picture = models.ImageField(upload_to='img')
    phone=models.CharField(max_length=32)
    fax=models.CharField(max_length=32)
    address = models.TextField()
    post_code=models.CharField(max_length=32)

class news(models.Model):
    title=models.CharField(max_length=32)
    time=models.DateField()
    description=models.TextField()
    image=models.ImageField(upload_to='img')
    content=models.TextField()
    type=models.CharField(max_length=32)


# Create your models here.
