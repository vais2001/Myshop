from django.shortcuts import render,redirect
from django .http import HttpResponse
from django.views import  View
from store.models.product import  Product

class Cart(View):
    def get(self , request):
        if request.session.get('cart'):
            ids = list(request.session.get('cart').keys())
            products = Product.get_products_by_id(ids)
            print(products)
            return render(request , 'cart.html' , {'products' : products} )
            #  return render(request , 'cart.html')
        else:
             return render(request,'cart.html')    