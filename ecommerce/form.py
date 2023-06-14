from .models import CustomUser,  Product
from django.forms import ModelForm

from django import forms
from django.contrib.auth.forms import UserCreationForm

# Creacion de usuario
class RegisterUser(UserCreationForm):
    email = forms.EmailField(label="Email")
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


