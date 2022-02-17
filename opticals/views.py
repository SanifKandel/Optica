
from django.shortcuts import render


def home(request):
    return render(request,"Home.html" )

def form(request):
    return render(request,"Form.html" )
    
def products(request):
    return render(request,"product.html" )

def sproducts(request):
    return render(request,"sproduct.html" )

def about(request):
    return render(request,"about.html" )

def contactus(request):
    return render(request,"contactus.html" )

def cart(request):
    return render(request,"cart.html" )
   
