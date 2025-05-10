from django.contrib import admin
from .models import Publicacion, AgentePublicacion, PublicacionTipoOper, PublicacionTipoProp

@admin.register(Publicacion)
class PublicacionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'cliente', 'barrio', 'tipo_propiedad', 'tipo_operacion', 'precio', 'moneda', 'ambientes')
    list_filter = ('tipo_operacion', 'tipo_propiedad', 'barrio', 'moneda')
    search_fields = ('titulo', 'descripcion', 'cliente__first_name', 'cliente__last_name', 'cliente__dni')
    ordering = ('-precio',)

    fieldsets = (
        (None, {'fields': ('titulo', 'cliente', 'barrio', 'tipo_propiedad', 'tipo_operacion')}),
        ('Detalles de la publicación', {'fields': ('descripcion', 'precio', 'moneda', 'ambientes')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('titulo', 'cliente', 'barrio', 'tipo_propiedad', 'tipo_operacion', 'descripcion', 'precio', 'moneda', 'ambientes')
        }),
    )

@admin.register(AgentePublicacion)
class AgentePublicacionAdmin(admin.ModelAdmin):
    list_display = ('agente', 'publicacion')
    search_fields = ('agente__first_name', 'agente__last_name', 'publicacion__titulo')

@admin.register(PublicacionTipoOper)
class PublicacionTipoOperAdmin(admin.ModelAdmin):
    list_display = ('publicacion', 'tipo_operacion')
    search_fields = ('publicacion__titulo', 'tipo_operacion__nombre')

@admin.register(PublicacionTipoProp)
class PublicacionTipoPropAdmin(admin.ModelAdmin):
    list_display = ('publicacion', 'tipo_propiedad')
    search_fields = ('publicacion', 'tipo_propiedad__nombre')