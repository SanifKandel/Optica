from django.shortcuts import redirect, render
from register.forms import CreateUserForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate,logout
from django.contrib import messages



def registerProcess(request):
        current_user = request.user
        if request.user.is_authenticated:
            return redirect ('index')
        else:
            form = CreateUserForm()

            if request.method == 'POST':
                print(request.POST)
                print("Got data")
                form = CreateUserForm(request.POST)
                if form.is_valid():
                    print("form valid")
                    form.save()
                    print("form saved")
                    # messages.success("New account created")
                    return redirect('login')
                    
                else:
                    messages.error(request, "Error")
            context={
                'form':form,
            }
        return render(request,"register.html",context)
        
        


            