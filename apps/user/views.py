from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView
from .models import User
from .forms import UserCreationForm

from django.contrib import messages

from django.contrib.auth import logout
from django.shortcuts import redirect


from django import forms
from django.contrib.auth.forms import AuthenticationForm


from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.views.generic import View


def not_authenticated(user):
    return not user.is_authenticated


class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label='email')


@method_decorator(user_passes_test(not_authenticated, login_url='home'), name='dispatch')
class UserLoginView(LoginView):
    template_name = 'auth/login.html'
    form_class = EmailAuthenticationForm

    def form_valid(self, form):
        messages.success(self.request, "Has iniciado sesión correctamente.")
        redirect_to = self.request.GET.get('next')
        if redirect_to:
            self.success_url = redirect_to
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Error al iniciar sesión. Por favor, verifica tus credenciales.")
        return super().form_invalid(form)

    def get_success_url(self):
        redirect_to = self.request.session.pop('next', None)
        if redirect_to:
            return redirect_to
        else:
            return self.success_url or reverse_lazy('home')


@method_decorator(user_passes_test(not_authenticated, login_url='home'), name='dispatch')
class UserRegisterView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'auth/register.html'
    success_url = '/login'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


def logout_view(request):
    logout(request)
    return redirect('home')  # reemplaza 'home' con la ruta a donde quieres redirigir al usuario después de cerrar sesión


def home_view(request):
    return render(request,"homepage/index.html")