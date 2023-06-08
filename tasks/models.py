from django import forms
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=150)
    is_pet_sitter = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='user_photos/', blank=True, null=True)
    location = models.CharField(max_length=150)

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email
        super().save(*args, **kwargs)


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=150)

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'is_pet_sitter',
                  'is_staff', 'photo', 'location', 'password1', 'password2']

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirm Password', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")

    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        username = cleaned_data['username']
        first_name = cleaned_data['first_name']
        last_name = cleaned_data['last_name']
        email = cleaned_data['email']
        is_pet_sitter = cleaned_data['is_pet_sitter']
        is_staff = cleaned_data['is_staff']
        photo = cleaned_data['photo']
        location = cleaned_data['location']
        password = cleaned_data['password1']

        user = CustomUser(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            is_pet_sitter=is_pet_sitter,
            is_staff=is_staff,
            photo=photo,
            location=location,
        )

        # Establecer la contraseña utilizando set_password
        user.set_password(password)

        if commit:
            user.save()

        return user
