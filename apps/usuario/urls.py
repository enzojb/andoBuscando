from django.urls import path
from apps.usuario.views import RegistroView, RegistroUsuarioView, PerfilView, EditarPerfilView, SoyAgenteView, EditarSoyAgenteView, CambiarContraseniaView, EditarContraseniaView, EliminarCuentaView

urlpatterns = [
    path("registro/", RegistroView.as_view(), name='registro'),
    path("registro_usuario/", RegistroUsuarioView.as_view(), name='registro_usuario'),
    path("perfil/", PerfilView.as_view(), name='perfil'),
    path("editar_perfil/", EditarPerfilView.as_view(), name='editar_perfil'),
    path("soy_agente/", SoyAgenteView.as_view(), name='soy_agente'),
    path("editar_soy_agente/", EditarSoyAgenteView.as_view(), name='editar_soy_agente'),
    path("cambiar_contrasenia/", CambiarContraseniaView.as_view(), name='cambiar_contrasenia'),
    path("editar_contrasenia/", EditarContraseniaView.as_view(), name='editar_contrasenia'),
    path("eliminar_cuenta/", EliminarCuentaView.as_view(), name='eliminar_cuenta'),
]
