from django.contrib import admin
from .models import Propiedad

@admin.register(Propiedad)
class PropiedadAdmin(admin.ModelAdmin):
    list_display = ('propiedad_foto','localidad','agente','tipo_propiedad','ambientes','dormitorios','banios','amenities','cochera','metros_cuadrados','precio','moneda','direccion','descripcion')
