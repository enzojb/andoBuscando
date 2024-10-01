from django.contrib import admin
from .models import Agente_busqueda

@admin.register(Agente_busqueda)
class Agente_busquedaAdmin(admin.ModelAdmin):
    list_display = ('agente','busqueda')
# Register your models here.
