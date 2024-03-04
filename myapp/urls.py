from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.index ,name='home'),
    path('home',views.index ,name='home'),
    path('donate',views.donate ,name='donate'),
    path('order',views.order ,name='order'),
    path('deliver',views.deliver ,name='deliver'),
    path('login',views.login ,name='login'),
    path('signup',views.signup ,name='signup'),
    path('logout',views.logout ,name='logout'),
]
