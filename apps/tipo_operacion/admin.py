from django.contrib import admin
from .models import TipoOperacion

@admin.register(TipoOperacion)
class TipoOperacionAdmin(admin.ModelAdmin):
    list_display = ('tipo_operacion')