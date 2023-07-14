from django.shortcuts import render,redirect
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password
from django.views import View

class Signup(View):
    def get(self,request):
         return render(request,'signup.html')
    def post(self,request):
         postData=request.POST
         print(postData)
         first_name=postData.get('firstname')
         print(first_name)
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
         print(customer)
         errormessage=self.validatecustomer(customer)
         
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
    def validatecustomer(self,customer):
         errormessage=None
         if not customer.first_name:
             errormessage='firstname is mustly required'
         elif len(customer.first_name)<2:
             errormessage='firstname should be  more than 2 characters'   
         elif not customer.last_name:
             errormessage=' lastname mustly required'
         elif len(customer.last_name)<3:
             errormessage='lastname should be more than 3 characters'
         elif not customer.phone:
             errormessage='plzzz enter phn number'
         elif len(customer.phone)<10:
             errormessage='number should be equal to 10 '
         elif not customer.password:
             errormessage='enter the password'    
         elif len(customer.password)<6:
             errormessage="password must be more than 6 char"    
         elif customer.isExists():
             errormessage='email is already registered'
         return errormessage
