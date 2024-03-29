from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'last_name', 'email', 'password1', 'password2', 'is_pet_sitter', 'photo', 'location']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
