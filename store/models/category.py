from django.db import models

class Category(models.Model):
    select=models.CharField(max_length=30,null=True)
    cls=models.CharField(max_length=30,default="high")
    def __str__(self):
        return self.select
    
    
    
    @staticmethod
    def get_all_categories():
     return Category.objects.all()
    