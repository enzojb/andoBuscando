from django.contrib import admin
from .models import PropiedadFoto

@admin.register(PropiedadFoto)
class Propiedad_fotoAdmin(admin.ModelAdmin):
    list_display = ('propiedad','ubicacion_url','descripcion_foto')
