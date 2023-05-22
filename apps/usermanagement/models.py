from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from apps.resources.utils import *
from .managers import CustomUserManager

class CustomUserPetOwnerManager(models.Manager):
    def get_queryset(self):
        return super(CustomUserPetOwnerManager,
                  self).get_queryset().filter(is_pet_sitter=False, is_deleted=False)




class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=20, unique=YES)
    last_name = models.CharField(max_length=100) 
    email = models.EmailField(_("email address"), unique=YES)
    is_staff = models.BooleanField(default=NOT)
    is_pet_sitter = models.BooleanField(null=YES)
    photo = models.ImageField(null=YES, blank=YES, default=USER_AVATAR_PATH) 
    location = models.CharField(max_length=150)
    is_deleted = models.BooleanField(default=NOT)
    date_joined = models.DateTimeField(auto_now_add=YES)
    
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    
    objects = CustomUserManager()
    fetch_pet_owners = CustomUserPetOwnerManager()
    
    def __str__(self):
        return self.email
  
class AccessControlManager(models.Manager):
    def valid_active_user(self, userkey):
        user_num = self.get(active_user=userkey)
        return user_num
      
class AccessControl(models.Model):
    active_user = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    objects = AccessControlManager()
    