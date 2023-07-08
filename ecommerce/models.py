from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

# Creacion de usuario
class CustomUser(AbstractUser):
    name = models.CharField(("Name"), max_length=50,null=True)
    email = models.EmailField(("Email"), max_length=254,null=True,unique=True)
    bio = models.TextField(("Description"),blank=True)
    avatar = models.ImageField(("Avatar"), upload_to=None,blank=True)

    USERNAME_FIELD = "email" or "name"
    REQUIRED_FIELDS = []


class Genre(models.Model):
    name = models.CharField(("Nombre"), max_length=50)
    
    def __str__(self) -> str:
        return self.name
    


class Product(models.Model):
    categorie = models.ManyToManyField(Genre, verbose_name=("Genero"),null=True,default=None)
    artist = models.CharField(("Artista"), max_length=50,null=True)
    name = models.CharField(("Nombre"), max_length=50,null=True)
    price = models.DecimalField(("Precio"), max_digits=5, decimal_places=2,null=True)
    image = models.ImageField(("Imagen"), upload_to='static/media', height_field=None, width_field=None, max_length=None,null=True)
    # list = models.ManyToManyField(car, verbose_name=_(""))
    duration = models.DecimalField(("Duracion"), max_digits=5, decimal_places=2,null=True,default=00)
    releasedate = models.DateField(("Fecha lanzado"), auto_now=False, auto_now_add=False,null=True)
    amount = models.PositiveIntegerField(("Cantidad"), default=1)
    cal = models.IntegerField(("Calificacion"),validators=[MinValueValidator(1), MaxValueValidator(5)],default=1)
    
    @property
    def get_discount(self):
        return '%2f' %(float(self.price) * float(self.amount))
        


    def __str__(self) -> str:
        return self.name


class car(models.Model):
    host = models.ForeignKey(CustomUser, verbose_name=("host"), on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name=("Product"), on_delete=models.CASCADE,null=True)
    carprice = models.DecimalField(("Price"), max_digits=5, decimal_places=2,null=True,default=1)
    caramount = models.PositiveIntegerField(("Cantidad"), default=1)
    created = models.DateTimeField(("Creacion"),auto_now_add=True,null=True)
    updated = models.DateTimeField(("Comentario actualizado"),auto_now=True)

    class Meta:
        ordering =  ['-updated','-created',]

    def __str__(self) -> str:
        # return self.product.name
        if self.product is not None:
            return self.product.name
        else:
            return "No product assigned"

    def get_costo(self):
        return self.carprice * self.caramount
    



class Comment(models.Model):
    host = models.ForeignKey(CustomUser, verbose_name=("Usuario"), on_delete=models.CASCADE)
    commentto = models.ForeignKey(Product, verbose_name=("Mensaje-en"), on_delete=models.CASCADE)
    body = models.TextField(("Mensaje"))
    created = models.DateField(("Publicado"),auto_now_add=True)


    def __str__(self) -> str:
        return self.body[0:50]