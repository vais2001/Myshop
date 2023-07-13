from django.urls import path
from .views import index 
from .views import signup
from .views import login
urlpatterns =[
    path('',index,name='homepage'),
    path('signup/',signup,name='signup'),
    path('login',login ,name='loginpage')
]
