from django.contrib import admin

# Register your models here.
from .models import Product,Category
class AdminProduct(admin.ModelAdmin):
    list_display=['productname','category','color','size','price','image']
class AdminCategory(admin.ModelAdmin):
    list_display=['select','cls']    
admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)
