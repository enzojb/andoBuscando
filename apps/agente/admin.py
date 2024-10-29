from django.contrib import admin
from .models import Agente

@admin.register(Agente)
class AgenteAdmin(admin.ModelAdmin):
    list_display = ('dni','telefono','matricula')
