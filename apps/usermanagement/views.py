from wsgiref.util import request_uri
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout,login
from apps.usermanagement.models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib import  messages
from django.urls import reverse_lazy
from apps.usermanagement.forms import RegisterForm, LoginForm
from django.views import generic
from django.contrib.auth import views as auth_views


# Create your views here.

def register(request):
  
    if request.user.is_authenticated:
        
        return redirect('home-page')
      
    if request.method == 'GET':
        form=RegisterForm()
        return render(request,'register/register.html',{
            'form' : form,'error':''
        })
    

    form = RegisterForm(request.POST, request.FILES)
    print("username: ", form.errors.get('username'))
         
    if request.method == 'POST' and form.is_valid():
        
        user = form.save()
        print("SITTER", user.last_name)
        if user:
            login(request,user)
            messages.success(request,'Cuenta creada exitosamente')
            return redirect('home-page')
    else:
        form=RegisterForm(request.POST)
        return render(request,'register/register.html',{
            'form' : form,'error':'datos incorrectos'
        })      


def petpal_login(request):
    if request.user.is_authenticated:
        return redirect('home-page')
    if request.method == 'GET':
        form = LoginForm()
        return render(request,'Login/Login.html',{
            'form' : form,'error':''
        })
    form = LoginForm(request=request, data=request.POST)
    
    if request.method == 'POST' and form.is_valid():
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
           login(request,user)
           return redirect('home-page')
        else:
            form = LoginForm()
            return render(request,'login/Login.html',{
                'form' : form,'error':'datos incorrectos'
            })
    else:
        form = LoginForm()
        return render(request,'Login/Login.html',{
            'form' : form,'error':'datos incorrectos'
        })          


def petpal_logout(request):
    if not request.user.is_authenticated:
        return render(request,'homepage/index.html')
    else:  
        if request.method == 'GET':
            logout(request)

            messages.success(request,'Salió de sesión exitosamente')
            return redirect('home-page')
          

    
    return render(request,'homepage/index.html')

