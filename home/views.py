from django.shortcuts import render
from product.models import featured ,Products


# Create your views here.

def index(request):
    featuredProducts = featured.objects.all()

    context={
        'featuredProducts':featuredProducts
    }
    
    return render(request, 'Home.html',context)

def product(request):
    ProductsCat = Products.objects.all()

    context={
        'ProductsCat':ProductsCat
    }
    return render(request, 'product.html',context)
