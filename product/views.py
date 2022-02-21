from django.shortcuts import render
from product.models import Products

# Create your views here.
def product(request):
    ProductsCat = Products.objects.all()

    context={
        'ProductsCat':ProductsCat
    }
    return render(request, 'product.html',context)