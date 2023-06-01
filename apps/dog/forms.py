from django import forms
from apps.dog.models import Dog
from apps.usermanagement.models import CustomUser
from django.core.exceptions import ValidationError
from apps.resources.utils import *

class AddDogForm(forms.ModelForm):
    #age = forms.IntegerField()
    photo = forms.ImageField(required=False)
          
    class Meta:
        model = Dog
        fields = ['name', 'age', 'breed','photo']
        exclude = ('dog_owner_id',)
        widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control',
                                       'required': 'true'}),
        'age': forms.TextInput({'class': 'form-control'}),
        
        'breed': forms.Select(attrs={'class': 'form-control'})
        
      }  
        
