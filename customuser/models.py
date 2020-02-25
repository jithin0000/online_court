from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.


user_choices = ( 
        ('Admin', 'Admin'),
        ('Lawyer', 'Lawyer'),
        ('Witness', 'Witness'),
        ('Member', 'Member'),
        )

class CustomUserManager(BaseUserManager):
    """ custom user manager for user """

    def create_user(self, email, username, user_type, password=None):
        """TODO: Docstring for create_user """

        if not email:
            raise ValuError("email is required field ")

        user = self.model(
               email = self.normalize_email(email),
               username=username,
               user_type=user_type,
                )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, user_type,password=None):
        """ create super user method """

        user = self.create_user(email, username,user_type, password)
        user.is_admin=True
        user.is_staff=True
        
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    """ customize user model """

    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    user_type=models.CharField(choices = user_choices, max_length=255)

    objects = CustomUserManager()

    is_admin = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username', 'user_type']


    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
