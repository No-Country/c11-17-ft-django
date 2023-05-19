from django import forms
from apps.dog.models import Dog
from apps.usermanagement.models import CustomUser
from django.core.exceptions import ValidationError
from apps.resources.utils import *

class AddDogForm(forms.ModelForm):
    name = forms.CharField(max_length=50)
    age = forms.IntegerField()
    breed = forms.ChoiceField(choices=BREEDS)
    photo = forms.ImageField(required=False)
          
    class Meta:
        model = Dog
        fields = ['name', 'age', 'breed','photo']
        exclude = ('dog_owner_id',)
        
        
          
            
       
        
