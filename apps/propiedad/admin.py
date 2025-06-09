from django.contrib import admin
from .models import Propiedad, PropiedadFoto, TipoPropiedad, TipoOperacion

@admin.register(Propiedad)
class PropiedadAdmin(admin.ModelAdmin):
    list_display = ('titulo','agente','foto','direccion', 'barrio', 'tipo_propiedad','tipo_operacion', 'precio', 'moneda', 'ambientes', 'metros_cuadrados', 'fecha_creacion', 'fecha_actualizacion')
    list_filter = ('tipo_propiedad', 'barrio', 'moneda') 
    search_fields = ('direccion', 'descripcion', 'barrio__barrio', 'tipo_propiedad__tipo_propiedad', 'tipo_operacion__tipo_operacion')
    ordering = ('-fecha_creacion',)

    fieldsets = (
        (None, {'fields': ('titulo','direccion', 'barrio', 'tipo_propiedad','tipo_operacion','foto', 'precio', 'moneda')}),
        ('Detalles de la propiedad', {'fields': ('descripcion', 'ambientes', 'metros_cuadrados')}),
    )

@admin.register(PropiedadFoto)
class PropiedadFotoAdmin(admin.ModelAdmin):
    list_display = ('propiedad', 'ubicacion_url', 'descripcion_foto')
    search_fields = ('propiedad__direccion', 'descripcion_foto')

@admin.register(TipoPropiedad)
class TipoPropiedadAdmin(admin.ModelAdmin):
    list_display = ('tipo_propiedad',)

@admin.register(TipoOperacion)
class TipoOperacionAdmin(admin.ModelAdmin):
    list_display = ('tipo_operacion',)
