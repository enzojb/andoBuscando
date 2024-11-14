from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Cliente
from django.core.exceptions import ValidationError

class ClienteForm(UserCreationForm):
    dni = forms.CharField(max_length=20, label="DNI")
    telefono = forms.CharField(max_length=20, label="Teléfono")

    class Meta:
        model = Cliente
        fields = ['username', 'first_name', 'last_name', 'dni', 'telefono', 'email', 'password1', 'password2']

class EditarPerfilForm(forms.ModelForm):
    password_current = forms.CharField(widget=forms.PasswordInput, label="Contraseña", required=True)

    class Meta:
        model = Cliente
        fields = ['username', 'first_name', 'last_name', 'dni', 'telefono', 'email']

    def clean_password_current(self):
        password = self.cleaned_data['password_current']
        if not self.instance.check_password(password):
            raise ValidationError("La contraseña actual introducida es incorrecta.")
        return password
    
class EditarContraseniaForm(UserCreationForm):
    password_current = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña actual'}), label="Contraseña actual", required=True)

    class Meta:
        model = Cliente
        fields = [] 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': 'Nueva contraseña'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': 'Confirmar nueva contraseña'})
    
    def clean_password_current(self):
        password_current = self.cleaned_data.get('password_current')
        if not self.instance.check_password(password_current):
            raise ValidationError("La contraseña actual introducida es incorrecta.")
        return password_current