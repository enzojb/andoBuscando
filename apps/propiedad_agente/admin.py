from django.contrib import admin
from .models import Propiedad_agente

@admin.register(Propiedad_agente)
class Propiedad_agenteAdmin(admin.ModelAdmin):
    list_display = ['propiedad_foto','localidad','tipo_propiedad','ambientes','dormitorios','banios','amenities','cochera','metros_cuadrados','precio','moneda','direccion','descripcion']
# Register your models here.
