from django.conf import settings
from django.db import models
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
    STATUS_CHOICES = [
        ('S', 'Solicitada'),
        ('A', 'Aceptada'),
        ('R', 'Rechazada'),
        ('C', 'Cancelada'),
    ]
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='S')
    sitter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
            validators=[validate_sitter], related_name='sitter_reservations')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,\
      validators=[validate_owner],related_name='owner_reservations')
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE,related_name='dog_reservations')
    total_cost = models.IntegerField(null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    
    
    
    
      