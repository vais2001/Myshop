from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models.product import Product
from .models.category import Category
def index(request):
    alproducts = Product.get_all_products()
    print(alproducts)
    alcategories=Category.get_all_categories()
    # return render(request,'orders.html')
    data={}
    data['products']=alproducts
    data['categories']=alcategories
    return render(request,'index.html',data)

