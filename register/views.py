from django.shortcuts import redirect, render
from register.forms import CreateUserForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate,logout
from django.contrib import messages



def registerProcess(request):
    return render(request,"register.html")
    # if request.method == 'POST' and 'register' in request.POST:
    #     current_user = request.user
    #     if request.user.is_authenticated:
    #         return redirect ('index')
    #     else:
    #         form = CreateUserForm()

    #         if request.method == 'POST':
    #             print(request.POST)
    #             print("Got data")
    #             form = CreateUserForm(request.POST)
    #             if form.is_valid():
    #                 print("form valid")
    #                 form.save()
    #                 print("form saved")
    #                 # messages.success("New account created")
    #                 return redirect('register')
                    
    #             else:
    #                 messages.error(request, "Error")
    #     context={
    #         'form':form,
    #     }
    #     return render(request,"Form.html",context)
        
        

    # elif request.method == 'POST' and 'login' in request.POST:
    #         if request.user.is_authenticated:
    #             return redirect ('index')
    #         else:
    #             if request.method == 'POST':
    #                 username = request.POST.get('username')
    #                 password = request.POST.get('password')

    #                 user = authenticate(request,username=username, password=password)

    #                 if username and password !="":
    #                     if user is not None:
    #                         auth_login(request,user)
    #                         return redirect('index')
    #                     else:
    #                         messages.info(request, "Username or password is incorrect")
    #                 else:
    #                     messages.info(request, "Enter username and password")
    #         return render(request,"Form.html",context)

    