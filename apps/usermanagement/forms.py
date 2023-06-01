from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from apps.usermanagement.models import CustomUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from apps.resources.utils import *

class RegisterForm(forms.Form):
    username = forms.CharField(label='Alias', required=True,
                                min_length=4, max_length=50,
                                widget=forms.TextInput(attrs={
                                    'id' : 'username',
                                }))
    last_name = forms.CharField(label='Apellido',
                                min_length=4, max_length=100,
                                widget=forms.TextInput(attrs={
                                    'id' : 'last_name',
                                }))
        
    email = forms.EmailField(label='Correo electrónico', required=True,
                            widget=forms.EmailInput(attrs={
                                'id' : 'email',
        }))
        
    user_role = forms.ChoiceField(label="Cuidador o Dueño?", 
                        choices=USER_ROLE) 
                         
      
    password = forms.CharField(label='Password', required=True,
                                widget=forms.PasswordInput(attrs={
                                    'id':'password'
                                }))
    photo = forms.ImageField(label='Photo', required=True)
                             
    location = forms.CharField(label='Ciudad', required=True,
                                min_length=4, max_length=50,
                                widget=forms.TextInput(attrs={
                                    'id' : 'ciudad',
                                }))
    
    class Meta:
      model = CustomUser
      fields=['username',
              'last_name', 
              'email', 
              'user_role',
              'password', 
              'photo', 
              'location']
      exclude = ['is_staff', 'is_deleted']
    
    def clean_username(self):
        username = self.cleaned_data.get('username')

        if CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError('El username ya se encuentra en uso')
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError('El email ya se encuentra en uso')
        return email

    def save(self):
        return CustomUser.objects.create_user(
            self.cleaned_data.get('email'),
            password = self.cleaned_data.get('password'),
            username = self.cleaned_data.get('username'),
            last_name = self.cleaned_data.get('last_name'),
            user_role = self.cleaned_data.get('user_role'),
            location = self.cleaned_data.get('location'),
            
        )
        

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email', required=True,
                               widget=forms.EmailInput(attrs={
                                'id' : 'email_username',
                                }))
    
    password = forms.CharField(label='Password', required=True,
                                widget=forms.PasswordInput(attrs={
                                    'id':'password'
                                }))
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
