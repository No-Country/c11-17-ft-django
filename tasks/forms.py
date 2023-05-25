from django import forms
from .models import CustomUser


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(required=True)
    is_pet_sitter = forms.BooleanField(required=False)
    is_staff = forms.BooleanField(required=False)
    photo = forms.ImageField(required=False)
    location = forms.CharField(max_length=150)
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
        last_name = cleaned_data['last_name']
        email = cleaned_data['email']
        is_pet_sitter = cleaned_data['is_pet_sitter']
        is_staff = cleaned_data['is_staff']
        photo = cleaned_data['photo']
        location = cleaned_data['location']
        password = cleaned_data['password1']

        user = CustomUser(
            username=username,
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
