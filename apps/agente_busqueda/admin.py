from django.contrib import admin
from .models import AgenteBusqueda

@admin.register(AgenteBusqueda)
class Agente_busquedaAdmin(admin.ModelAdmin):
    list_display = ('agente','busqueda')
# Register your models here.
