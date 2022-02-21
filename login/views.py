from django.shortcuts import redirect, render
from register.forms import CreateUserForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate,logout
from django.contrib import messages


# Create your views here.
def loginProcess(request):
    if request.user.is_authenticated:
        return redirect ('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request,username=username, password=password)

            if username and password !="":
                if user is not None:
                    auth_login(request,user)
                    return redirect('index')
                else:
                    messages.info(request, "Username or password is incorrect")
            else:
                messages.info(request, "Enter username and password")

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('index')
