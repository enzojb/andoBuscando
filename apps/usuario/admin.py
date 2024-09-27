from django.contrib import admin

from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido','correo','contraseña')

# Register your models here.
