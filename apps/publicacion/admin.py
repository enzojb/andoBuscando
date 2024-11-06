from django.contrib import admin
from .models import Publicacion

@admin.register(Publicacion)
class PublicacionAdmin(admin.ModelAdmin):
    list_display = ('cliente','localidad','tipo_propiedad','tipo_operacion','titulo','ambientes','precio','moneda','descripcion')