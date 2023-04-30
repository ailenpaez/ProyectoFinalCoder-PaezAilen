from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import Entrenamiento
from django.contrib.auth.models import User

class Contacto(forms.Form):
     entrenamiento = forms.CharField()
     nivel = forms.IntegerField()
    
    
class ProfeForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=254)
    deporte = forms.CharField(max_length=50)
    
class UserEditForm(UserChangeForm):
    
    password=forms.CharField(
        help_text="",
        widget=forms.HiddenInput(), required=False
    )

    password1=forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2=forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model=User
        fields=('email','first_name','last_name','password1','password2')
        
def clean_password2(self):
    print(self.cleaned_data)
        
    password2= self.cleaned_data['password2']
    if password2 !=  self.cleaned_data['password1']:
        raise forms.ValidationError('Las contraseñas no coinciden!')
    return password2
    
        


    
    
    