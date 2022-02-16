from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('form',views.form,name='form'),
    path('products',views.products,name='products'),
    path('sproducts',views.sproducts,name='sproducts'),
     path('about',views.about,name='about'),

]
