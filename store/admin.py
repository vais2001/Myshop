from django.contrib import admin

from .models import Product,Category,Customer
# Register your models here.
class AdminProduct(admin.ModelAdmin):
    list_display=['productname','category','color','size','price','image']
class AdminCategory(admin.ModelAdmin):
    list_display=['select','cls']   
class AdminCustomer(admin.ModelAdmin):
    list_display=['first_name','last_name','phone','email']     
admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)
admin.site.register(Customer,AdminCustomer)
