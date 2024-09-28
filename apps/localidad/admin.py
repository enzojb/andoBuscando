from django.contrib import admin
from .models import Localidad

@admin.register(Localidad)
class LocalidadAdmin(admin.ModelAdmin):
    list_display = ('localidad')