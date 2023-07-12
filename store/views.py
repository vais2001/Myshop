from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models.product import Product
from .models.category import Category
def index(request):
    alproducts = None
    print(alproducts)
    alcategories=Category.get_all_categories()
    categoryId=request.GET.get('category')
    if categoryId:
         alproducts=Product.get_all_products_by_categoryid(categoryId)    
    else:
        alproducts=Product.get_all_products()
    # return render(request,'orders.html')
    data={}
    data['products']=alproducts
    data['categories']=alcategories
    return render(request,'index.html',data)

def signup(request):
    return render(request,'signup.html')
    
 