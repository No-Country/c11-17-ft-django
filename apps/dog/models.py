from django.db import models
from django.db.models import Q
from apps.resources.utils import *
from django.conf import settings


class Dog(models.Model):
    dog_owner_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='dogs')
    name = models.CharField(max_length=50, unique=True)
    age = models.IntegerField()
    breed = models.CharField(max_length=30,choices=BREEDS, default=BREEDS[0][1])
    photo = models.ImageField(null=YES, blank=YES, default=BREED_AVATAR_PATH) 
    
    class Meta:
        ordering = ('-name',)
    
    def __str__(self):
        return self.name