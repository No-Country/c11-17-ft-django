from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from .models import User
from .forms import UserCreationForm

from django.contrib import messages

class UserLoginView(LoginView):
    template_name = 'auth/login.html'

    def form_valid(self, form):
        messages.success(self.request, "Has iniciado sesión correctamente.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Error al iniciar sesión. Por favor, verifica tus credenciales.")
        return super().form_invalid(form)


class UserRegisterView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'auth/register.html'
    success_url = '/login'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
