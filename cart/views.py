import json
from django.http import JsonResponse
from django.shortcuts import render
from cart.models import Order, OrderedItems

from product.models import Products

# Create your views here.
def cart(request):
    return render(request,"cart.html")

def contactus(request):
    return render(request,"contactus.html")

def about(request):
    return render(request,"about.html")

def addToCart(request):
    data = json.loads(request.body)
    product = data['product']
    action = data['action']

    print(action)

    customer = request.user
    product = Products.objects.get(id=product)
    order, created = Order.objects.get_or_create(user_details = customer,  completed=False)

    orderItem,created = OrderedItems.objects.get_or_create(order=order,product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    elif action == 'deleteItem':
        orderItem.quantity = 0

    orderItem.save()


    if orderItem.quantity <=0:
        orderItem.delete()

    # return redirect ('index')

    return JsonResponse('HREER', safe=False)

def viewCart(request):
    print("ENTERED VIEWCART")
    customer = request.user
    order, created = Order.objects.get_or_create(user_details = customer, completed=False)
    items = order.ordereditems_set.all()
    print(items)
    context={
        'items':items,
        'order':order,
        
    }
    return render(request, 'cart.html', context)






