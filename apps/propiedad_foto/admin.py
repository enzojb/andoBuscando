from django.contrib import admin
from .models import Propiedad_foto

@admin.register(Propiedad_foto)
class Propiedad_fotoAdmin(admin.ModelAdmin):
    list_display = ('propiedad','ubicacion_url','descripcion_foto')
