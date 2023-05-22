from django.db import models
from django.db.models import Q
from apps.resources.utils import *
from apps.usermanagement.models import CustomUser
# Create your models here.


class Dog(models.Model):
    dog_owner_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True)
    age = models.IntegerField()
    breed = models.CharField(max_length=30,choices=BREEDS, default=BREEDS[0][1])
    photo = models.ImageField(null=YES, blank=YES, default=BREED_AVATAR_PATH) 
    
    class Meta:
        ordering = ('-name',)
    
    def __str__(self):
        return self.name