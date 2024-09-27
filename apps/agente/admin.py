from django.contrib import admin
from .models import Agente

@admin.register(Agente)
class agenteAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido','correo','contraseña','dni','telefono','matricula')
# Register your models here.
