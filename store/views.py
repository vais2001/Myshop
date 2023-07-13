from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from django.contrib.auth.hashers import make_password,check_password

# Create your views here.
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



def validatecustomer(customer):
         errormessage=None
         if not customer.first_name:
             errormessage='firstname is mustly required'
         elif len(customer.first_name)<2:
             errormessage='firstname should be  more then 2 characters'   
         elif not customer.last_name:
             errormessage=' lastname mustly required'
         elif len(customer.last_name)<3:
             errormessage='lastname should be more then 3 characters'
         elif not customer.phone:
             errormessage='plzzz enter phn number'
         elif len(customer.phone)==10:
             errormessage='number should be equal to 10 '
         elif not customer.password:
             errormessage='enter the password'    
         elif len(customer.password)<6:
             errormessage="password must be more then 6 char"    
         elif customer.isExists():
             errormessage='email is already is exit'
         return errormessage
     
     
        # for POST request    
def registeruser(request):
         postData=request.POST
         first_name=postData.get('firstname')
         last_name=postData.get('lastname')
         phone=postData.get('phone')
         email=postData.get('email')
         password=postData.get('password')  
         value={
            'first_name':first_name,
            'last_name':last_name,
            'phone':phone,
            'email':email
         }       
         customer=Customer(first_name=first_name,
                           last_name=last_name,
                           phone=phone,
                           email=email,
                           password=password)
         errormessage=validatecustomer(customer)
         
            #saving(customer register)
         if not errormessage:     
            print(first_name,last_name,phone,email)
            customer.password=make_password(customer.password)
            customer.register()
            return redirect('homepage')
         else:
             data={
                 'error':errormessage,
                 'values':value
             }
             return render(request,'signup.html',data)                             
def signup(request):
    if request.method=='GET':
        return render(request,'signup.html')
    else:
         return registeruser(request)



def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        email=request.POST.get('email')
        password=request.POST.get('password')
        customer=Customer.get_customer_by_email(email)
        # print(customer)
        errormessage=None
        if customer:
            flag=check_password(password,customer.password)
            if flag:
              return redirect('homepage')
            else:
                  errormessage='Email or password invalid'
        else:
            errormessage='Email or password invalid'
        print(email,password)
        return render (request,'login.html',{'error':errormessage})