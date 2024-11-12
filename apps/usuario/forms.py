from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Cliente

class ClienteForm(UserCreationForm):
    dni = forms.CharField(max_length=20, label="DNI")
    telefono = forms.CharField(max_length=20, label="Teléfono")

    class Meta:
        model = Cliente
        fields = ['username', 'first_name', 'last_name', 'dni', 'telefono', 'email', 'password1', 'password2']