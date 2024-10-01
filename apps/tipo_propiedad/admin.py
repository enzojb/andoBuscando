from django.contrib import admin
from .models import Tipo_Propiedad

@admin.register(Tipo_Propiedad)
class Tipo_PropiedadAdmin(admin.ModelAdmin):
    list_display = ('tipo_propiedad',)