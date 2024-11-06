from django.contrib import admin
from .models import Propiedad
from .models import Localidad
from .models import TipoPropiedad
from .models import TipoOperacion

@admin.register(Propiedad)
class PropiedadAdmin(admin.ModelAdmin):
    list_display = ('localidad','agente','ambientes','metros_cuadrados','precio','moneda','direccion','descripcion')

@admin.register(Localidad)
class LocalidadAdmin(admin.ModelAdmin):
    list_display=('localidad',)

@admin.register(TipoOperacion)
class TipoOperacionAdmin(admin.ModelAdmin):
    list_display=('tipo_operacion',)

@admin.register(TipoPropiedad)
class TipoPropiedadAdmin(admin.ModelAdmin):
    list_display=('tipo_propiedad',)