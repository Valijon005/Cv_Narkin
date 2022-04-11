from django.contrib import admin
from django.urls import path
from Myapp.views import *

urlpatterns = [
    path('Home', Home,  name='tushganpul'),
    path('', checkout, name='checkout'),
    path('home', checkout, name='Chec')
       
]