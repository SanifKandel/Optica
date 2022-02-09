from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request,"Home.html" )

def form(request):
    return render(request,"Form.html" )

