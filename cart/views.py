from django.shortcuts import render

# Create your views here.
def cart(request):
    return render(request,"cart.html")

def contactus(request):
    return render(request,"contactus.html")

def about(request):
    return render(request,"about.html")
