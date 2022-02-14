
from django.shortcuts import render


def home(request):
    return render(request,"Home.html" )

def form(request):
    return render(request,"Form.html" )
    
def products(request):
    return render(request,"product.html" )

