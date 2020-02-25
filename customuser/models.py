from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class CustomUserManager(BaseUserManager):
    """ custom user manager for user """
    pass