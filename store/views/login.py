from django.shortcuts import render,redirect,HttpResponseRedirect
from store.models.customer import Customer
from django.contrib.auth.hashers import check_password
from django.views import View
# loginviews
class Login(View):
    return_url=None
    def get(self,request):
       Login.return_url=request.GET.get('return_url')
       return render(request,'login.html')
    def post(self,request):
        email=request.POST.get('email')
        password=request.POST.get('password')
        customer=Customer.get_customer_by_email(email)
        # print(customer)
        errormessage=None
        if customer:
            flag=check_password(password,customer.password)
            # print(flag)
            if flag:
                request.session['customer']=customer.id
                # request.session['email']=customer.email
                # 
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url=None
                    return redirect('homepage')
            else:
                  errormessage='Email or password invalid'
        else:
            errormessage='Email or password invalid'
        # print(email,password)
        return render (request,'login.html',{'error':errormessage})
def logout(request):
    request.session.clear()
    return redirect('loginpage') 