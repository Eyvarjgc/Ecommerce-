from django.shortcuts import render,redirect
from .form import RegisterUser
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout

# Create your views here.



def home(request):
    # context = []

    return render(request,'home.html')


def login(request):
    return render(request,'registration/login.html')

def register(request):
    form = RegisterUser()
    if request.method == 'POST':
        form = RegisterUser(request.POST)
        if form.is_valid:
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')
        else:
                messages.error(request,'no ha ingresado las contraseñas correctamente')
    context = {
        'form':form,
    }
    return render(request, 'register.html',context)

def LogoutUser(request):
    logout(request)
    return redirect(home)