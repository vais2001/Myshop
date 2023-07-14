from django.shortcuts import render,redirect
from store.models.customer import Customer
from django.contrib.auth.hashers import check_password
from django.views import View
# loginviews
class Login(View):
    def get(self,request):
       return render(request,'login.html')
    def post(self,request):
        email=request.POST.get('email')
        password=request.POST.get('password')
        customer=Customer.get_customer_by_email(email)
        # print(customer)
        errormessage=None
        if customer:
            flag=check_password(password,customer.password)
            print(flag)
            if flag:
              return redirect('homepage')
            else:
                  errormessage='Email or password invalid'
        else:
            errormessage='Email or password invalid'
        print(email,password)
        return render (request,'login.html',{'error':errormessage})
