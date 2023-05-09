from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# from .manager import UserManager


# Create your models here.

class User(AbstractUser):
    
    is_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=4, null=True, blank=True)   
    
    def __str__(self):
        return super().email
    