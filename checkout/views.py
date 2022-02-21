from django.http import JsonResponse
from django.shortcuts import redirect, render

from cart.models import Order
from checkout.models import ShippingDetails

# Create your views here.
def checkout(request):
    customer = request.user
    order, created = Order.objects.get_or_create(user_details = customer, completed=False)
    items = order.ordereditems_set.all()
    print(items)
    context={
        'items':items,
        'order':order,
        
    }
    return render(request, 'checkoutpage.html',context)

def saveshippingdetails(request):
    if request.method == 'POST':
        orderid = request.POST.get('orderid')
        orderid = Order.objects.get(id=orderid)
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        postal_code = request.POST.get('postalcode')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')

        print(full_name)
        print(email)
        print(phone)
        print(address)
        print(city)
        print(state)
        print(postal_code)

        saveData = ShippingDetails(user_data=request.user,o_ID=orderid,fullname=full_name, phone=phone, email=email, city=city,address=address,state=state,postalcode=postal_code)
        saveData.save()
        orderid.completed=True
        orderid.save()

    return redirect('index')

    

