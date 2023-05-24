from django.db import models
from apps.usermanagement.models import CustomUser
from apps.dog.models import Dog
from django.core.exceptions import ValidationError
# Create your models here.
def validate_owner(value):
    if value == True:
      raise ValidationError('Debe ser un dueño de perro')

def validate_sitter(value):
  if value == False:
      raise ValidationError('Debe ser cuidador de perro')
    
class Reservation(models.Model):
    sitter = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
            validators=[validate_sitter], related_name='sitter_reservations')
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE,\
      validators=[validate_owner],related_name='owner_reservations')
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE,related_name='dog_reservations')
    total_cost = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    
    
    
    
      