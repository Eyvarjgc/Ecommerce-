from .models import CustomUser,  Product
from django.forms import ModelForm

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import SetPasswordForm,AuthenticationForm,PasswordResetForm
from django.contrib.auth import get_user_model
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

    # def __init__(self,*args,**kargs):
    #     super().__init__(*args,**kargs)
    #     self.fields['name'].widget.attrs.update({'class': 'form-control'})

class changepassword(SetPasswordForm):
    class Meta:
        model = get_user_model()
        fields = ['newpassword1', 'newpassword2']

class PasswordResetForm(PasswordResetForm):
    def __init__(self,*args,**kwargs):
        super(PasswordResetForm, self).__init__(*args,**kwargs)