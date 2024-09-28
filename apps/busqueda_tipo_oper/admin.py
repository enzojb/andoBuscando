from django.contrib import admin
from .models import BusquedaTipoOper

@admin.register(BusquedaTipoOper)
class BusquedaTipoOperAdmin(admin.ModelAdmin):
    list_display = ('busqueda','tipo_operacion')