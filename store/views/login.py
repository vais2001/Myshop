from django.shortcuts import render,redirect,HttpResponse
from store.models.customer import Customer
from django.contrib.auth.hashers import check_password
from django.views import View
# loginviews
class Login(View):
    def get(self,request):
       return render(request,'login.html')
    def post(self,request):
        print(111111111111111111111111111,request)
        email=request.POST.get('email')
        password=request.POST.get('password')
        customer=Customer.get_customer_by_email(email)
        print(222222222222222222222222222222222,customer)
        errormessage=None

        if customer:
            flag=check_password(password,customer.password)
            print(flag)
            if flag:
              request.session['customer_id']=customer.id
              request.session['customer_email']=customer.email
                
              return redirect('homepage') 
            else:
                  errormessage='Email or password invalid'
        else:
            errormessage='Email or password invalid'
        print(email,password)
        return render (request,'login.html',{'error':errormessage})
