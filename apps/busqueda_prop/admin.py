from django.contrib import admin
from .models import Busqueda_prop

@admin.register(Busqueda_prop)
class Busqueda_propAdmin(admin.ModelAdmin):
    list_display = ['agente','propiedad']
# Register your models here.
