from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models.product import Product
def index(request):
    alproducts = Product.get_all_products()
    print(alproducts)
    
    return render(request,'index.html',{'products':alproducts})

