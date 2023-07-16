from django.shortcuts import render
from store.models.product import Product
from store.models.category import Category
# from django.views import 

def index(request):
    # alproducts = None
    # print(alproducts)
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
    print(request.session.get('customer_email'))
    return render(request,'index.html',data)
