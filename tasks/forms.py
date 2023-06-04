from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

CITIES_LATIN_AMERICA = [
    ('Buenos Aires', 'Buenos Aires'),
    ('Sao Paulo', 'Sao Paulo'),
    ('Ciudad de México', 'Ciudad de México'),
    # Agrega más ciudades de América Latina según sea necesario
]


class RegistrationForm(UserCreationForm):
    is_pet_sitter = forms.BooleanField(required=False)
    photo = forms.ImageField(required=False)
    location = forms.ChoiceField(choices=CITIES_LATIN_AMERICA, required=False)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'is_pet_sitter',
                  'is_staff', 'photo', 'location', 'password1', 'password2']
        widgets = {
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'password1': 'Password',
            'password2': 'Confirm Password',
        }
        help_texts = {
            'username': None,
        }
        error_messages = {
            'password1': {
                'required': 'Please enter a password.',
            },
            'password2': {
                'required': 'Please confirm your password.',
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['is_pet_sitter'].label = 'Are you a pet sitter?'
        self.fields['password2'].label = 'Confirm Password'
        self.fields['is_staff'].label = 'Are you part of the staff?'
        self.fields['password2'].help_text = ''

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_pet_sitter = self.cleaned_data.get('is_pet_sitter', False)
        user.is_staff = self.cleaned_data.get('is_staff', False)
        user.photo = self.cleaned_data.get('photo', None)
        user.location = self.cleaned_data.get('location', '')

        if commit:
            user.save()

        return user

    def clean_username(self):
        username = self.cleaned_data['username']
        existing_user = CustomUser.objects.exclude(
            pk=self.instance.pk).filter(username=username)
        if existing_user.exists():
            raise forms.ValidationError(
                'A user with that username already exists.')
        return username
