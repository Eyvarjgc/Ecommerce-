from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

# Creacion de usuario
class User(AbstractBaseUser):
    name = models.CharField(("Name"), max_length=50,null=True)
    email = models.EmailField(("Email"), max_length=254,null=True,unique=True)
    bio = models.TextField(("Description"),blank=True)
    avatar = models.ImageField(("Avatar"), upload_to=None)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

