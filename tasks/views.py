from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import RegistrationForm


# Create your views here.


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'GET':
        form = RegistrationForm()
        return render(request, 'signup.html', {'form': form})
    else:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password1'] == form.cleaned_data['password2']:
                try:
                    user = form.save()
                    login(request, user)
                    return redirect('tasks')
                except IntegrityError:
                    error = 'Este usuario ya existe'
            else:
                error = 'El password es incorrecto'
        else:
            error = 'Hubo un error en el formulario. Por favor, verifica los campos ingresados.'

        return render(request, 'signup.html', {'form': form, 'error': error})


def tasks(request):
    return render(request, 'tasks.html')


def signout(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o pass incorrecto '
            })

        else:
            login(request, user)
            return redirect('tasks')
