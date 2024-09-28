from django.contrib import admin
from .models import BusquedaTipoProp

@admin.register(BusquedaTipoProp)
class BusquedaTipoPropAdmin(admin.ModelAdmin):
    list_display = ('busqueda','tipo_propiedad')