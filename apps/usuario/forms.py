from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import Usuario
from django.core.exceptions import ValidationError

class UsuarioForm(UserCreationForm):
    dni = forms.CharField(max_length=20, label="DNI")
    telefono = forms.CharField(max_length=20, label="Teléfono")

    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'dni', 'telefono', 'email', 'password1', 'password2']

class EditarPerfilForm(forms.ModelForm):
    password_current = forms.CharField(widget=forms.PasswordInput, label="Contraseña", required=True)

    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'dni', 'telefono', 'email']

    def clean_password_current(self):
        password = self.cleaned_data['password_current']
        if not self.instance.check_password(password):
            raise ValidationError("La contraseña actual introducida es incorrecta.")
        return password
    
class EditarSoyAgenteForm(forms.ModelForm):
    password_current = forms.CharField(widget=forms.PasswordInput, label="Contraseña", required=True)

    class Meta:
        model = Usuario
        fields = ['is_agente', 'matricula']

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
        model = Usuario
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