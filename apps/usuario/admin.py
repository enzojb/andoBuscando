from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Agente, Cliente, Moderador

# Personalizar el admin para el Usuario
@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'dni', 'telefono', 'get_user_type', 'is_staff', 'is_active', 'date_joined')
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    search_fields = ('username', 'first_name', 'last_name', 'email', 'dni')
    ordering = ('-date_joined',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),  # Usuario
        ('Información Personal', {'fields': ('first_name', 'last_name', 'email', 'dni', 'telefono')}),  # Información Personal
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),  # Permisos
        ('Fechas importantes', {'fields': ('last_login', 'date_joined')}),  # Fechas importantes
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'dni', 'telefono', 'is_staff', 'is_active'),
        }),
    )
    filter_horizontal = ('groups', 'user_permissions')

    def get_user_type(self, obj):
        # Verificar si el objeto es una instancia de Agente, Cliente o Moderador
        if isinstance(obj, Agente):
            return 'Agente'
        elif isinstance(obj, Cliente):
            return 'Cliente'
        elif isinstance(obj, Moderador):
            return 'Moderador'
        return 'Desconocido'
    
    get_user_type.short_description = 'Tipo de usuario'  # Personalizamos el encabezado para este campo

# Personalizar el admin para Agente
@admin.register(Agente)
class AgenteAdmin(UsuarioAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'dni', 'telefono', 'matricula', 'is_staff', 'is_active', 'date_joined')
    search_fields = ('username', 'first_name', 'last_name', 'email', 'dni', 'matricula')

# Personalizar el admin para Cliente
@admin.register(Cliente)
class ClienteAdmin(UsuarioAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'dni', 'telefono', 'is_staff', 'is_active', 'date_joined')
    search_fields = ('username', 'first_name', 'last_name', 'email', 'dni')

# Personalizar el admin para Moderador
@admin.register(Moderador)
class ModeradorAdmin(UsuarioAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'dni', 'telefono', 'is_staff', 'is_active', 'date_joined')
    search_fields = ('username', 'first_name', 'last_name', 'email', 'dni')
