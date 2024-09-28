from django.contrib import admin
from .models import TipoPropiedad

@admin.register(TipoPropiedad)
class TipoPropiedadAdmin(admin.ModelAdmin):
    list_display = ('tipo_propiedad')