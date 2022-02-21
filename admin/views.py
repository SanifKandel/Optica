from django.shortcuts import redirect, render
from cart.models import Order, OrderedItems
from cart.views import cart
from checkout.models import ShippingDetails
from product.forms import productfield

from product.models import Products

# Create your views here.
def adminOrder(request):

    orderitems = OrderedItems.objects.all()

    return render(request,"adminorders.html",{'orderitems':orderitems})

def adminProducts(request):

    allProducts = Products.objects.all()

    context={
        'allProducts':allProducts,
    }

    return render(request,'adminproducts.html',context)


def productadd(request):
    if request.method == 'POST':
        form = productfield(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            print('form save')
            print('success')
            return redirect('adminProduct')
    else:
        form = productfield()

    context={
        'form':form,
    }
    return render(request,'productadd.html',context)

def adminCart(request):

    allcarts = ShippingDetails.objects.all()

    context={
        'allcarts':allcarts,
    }

    return render(request,'adminusers.html',context)

def deleteorder(request):
    if request.method == 'POST':
        id = request.POST['id']
        dlt =Order.objects.get(id=id).delete()
        dlt.save()
    return redirect('/customadmin/Order/')