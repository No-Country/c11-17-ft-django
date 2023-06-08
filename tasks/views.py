from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth import update_session_auth_hash
from django.db import IntegrityError
from .forms import RegistrationForm


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            # Redirigir a la página de inicio si el usuario ya está autenticado
            return redirect('inicio')
        form = RegistrationForm()
        return render(request, 'signup.html', {'form': form, 'user': request.user})
    else:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            if password1 == password2:
                try:
                    user = form.save()
                    login(request, user)
                    if user.is_pet_sitter:
                        return render(request, 'buscar_perro.html', {'user': user})
                    else:
                        return render(request, 'buscar_paseador.html', {'user': user})
                except IntegrityError:
                    error = 'Este usuario ya existe'
            else:
                error = 'Las contraseñas no coinciden'
        else:
            error = 'Hubo un error en el formulario. Por favor, verifica los campos ingresados.'

        return render(request, 'signup.html', {'form': form, 'error': error, 'user': request.user})


def signout(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {'form': AuthenticationForm(), 'user': request.user})
    else:
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            if user.is_pet_sitter:
                return render(request, 'buscar_perro.html')
            else:
                return render(request, 'buscar_paseador.html')

        else:
            return render(request, 'signin.html', {'form': form, 'error': 'Usuario o contraseña incorrectos', 'user': request.user})


def buscar_paseador(request):
    # Lógica de la vista para la página "Buscar paseador"
    return render(request, 'buscar_paseador.html')


def buscar_perro(request):
    # Lógica de la vista para la página "Buscar perro"
    return render(request, 'buscar_perro.html')


def modpro(request):
    # Lógica de la vista para la página "modpro"
    return render(request, 'modpro.html')


def modpro(request):
    user = request.user
    if request.method == 'POST':
        form = RegistrationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            # Actualizar sesión de autenticación
            update_session_auth_hash(request, user)
            return redirect('home')  # Redirigir a la página de inicio
    else:
        form = RegistrationForm(instance=user)
    return render(request, 'modpro.html', {'form': form})
