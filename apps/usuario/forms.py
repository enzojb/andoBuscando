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
    
class EditarContraseniaForm(forms.ModelForm):
    password_current = forms.CharField(widget=forms.PasswordInput, label="Contraseña actual", required=True)
    password = forms.CharField(widget=forms.PasswordInput, label="Nueva contraseña", required=True)
    repassword = forms.CharField(widget=forms.PasswordInput, label="Confirmar nueva contraseña", required=True)

    class Meta:
        model = Cliente
        fields = ['password'] 

    def clean_password_current(self):
        password = self.cleaned_data['password_current']
        if not self.instance.check_password(password):
            raise ValidationError("La contraseña actual introducida es incorrecta.")
        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        repassword = cleaned_data.get('repassword')

        if password and repassword and password != repassword:
            raise ValidationError("Las nuevas contraseñas no coinciden.")
        
        return cleaned_data