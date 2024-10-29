from django.contrib import admin
from .models import Moderador

@admin.register(Moderador)
class ModeradorAdmin(admin.ModelAdmin):
    list_display = ()