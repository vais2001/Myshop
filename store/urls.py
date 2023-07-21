from django.urls import path
from .views.home import Index 
from .views.signup import Signup
from .views.login import Login,logout
from .views.cart import Cart
from .views.check_out import check_out
from .views.orders import OrderView
from store.middlewares.auth import auth_middleware
urlpatterns =[
    path('',Index.as_view(),name='homepage'),
    path('signup/',Signup.as_view(),name='signup'),
    path('login',Login.as_view() ,name='loginpage'),
    path('logout',logout,name='logout'),
    path('cart',Cart.as_view(),name='cart'),
    path('check-out',check_out.as_view(),name='check_out'),
    path('orders',auth_middleware (OrderView.as_view()),name='checkorder'),
]
