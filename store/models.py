from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)

class Product(models.Model):
    productname=models.CharField(max_length=30)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    color=models.CharField(max_length=20)
    size=models.CharField(max_length=20)
    price=models.IntegerField(default=0)
  

