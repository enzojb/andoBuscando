from django.contrib import admin
from .models import Busqueda

@admin.register(Busqueda)
class BusquedaAdmin(admin.ModelAdmin):
    list_display = ('cliente','localidad','ambientes','dormitorios','banios','amenities','cochera','metros_cuadrados','precio','moneda')