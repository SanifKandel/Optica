from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [

    
    path('user-cart/',views.viewCart,name="cartIndex"),
    path('contactus/',views.contactus,name="contactus"),
    path('about/',views.about,name="about")
      
   
]