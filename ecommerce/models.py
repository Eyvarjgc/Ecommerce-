from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# Creacion de usuario
class CustomUser(AbstractUser):
    name = models.CharField(("Name"), max_length=50,null=True)
    email = models.EmailField(("Email"), max_length=254,null=True,unique=True)
    bio = models.TextField(("Description"),blank=True)
    avatar = models.ImageField(("Avatar"), upload_to=None,blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Product(models.Model):
    name = models.CharField(("Nombre"), max_length=50,null=True)
    price = models.FloatField(("Precio"),null=True)
    image = models.ImageField(("Imagen"), upload_to='static/media', height_field=None, width_field=None, max_length=None,null=True)
    # list = models.ManyToManyField(car, verbose_name=_(""))

    def __str__(self) -> str:
        return self.name
class car(models.Model):
    host = models.ForeignKey(CustomUser, verbose_name=("host"), on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name=("Product"), on_delete=models.CASCADE,null=True)
    
    def __str__(self) -> str:
        # return self.product.name
        if self.product is not None:
            return self.product.name
        else:
            return "No product assigned"





    # def __str__(self) -> str:
    #     return f"{self.host} - {self.product}"