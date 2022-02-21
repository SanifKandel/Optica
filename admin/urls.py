from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('Order/',views.adminOrder,name="adminOrder"),
    path('Product/',views.adminProducts,name="adminProduct"),
    path('Cart/',views.adminCart,name="adminCart"),
    path('deleteOrder/',views.deleteorder,name="deleteOrder"),
    path('addproduct/',views.productadd,name="productadd"),

       
]