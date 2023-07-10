from django.db import models
from .category import Category

class Product(models.Model):
    productname=models.CharField(max_length=30)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    color=models.CharField(max_length=30)
    size=models.CharField(max_length=10)
    price=models.IntegerField(default=0)
    image=models.ImageField(upload_to='uploads/products/',default=False)
    def __str__(self):
      return self.productname
    def __str__(self):
      return self.color
    def __str__(self):
      return self.size
  

    @staticmethod
    def get_all_products():
     return Product.objects.all()

   