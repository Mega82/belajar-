from unicodedata import name
from django.urls import path
from . import views

urlpattersns - (
    path('',views.awal,name='awal')
    path('home',views.home,name='home')
)