from django.urls import path
from apps.usuario.views import RegistroView, PerfilView, SoyAgenteView, CambiarContraseniaView, EliminarCuentaView

urlpatterns = [
    path("registro/", RegistroView.as_view(), name='registro'),
    path("perfil/", PerfilView.as_view(), name='perfil'),
    path("soy_agente/", SoyAgenteView.as_view(), name='soy_agente'),
    path("cambiar_contrasenia/", CambiarContraseniaView.as_view(), name='cambiar_contrasenia'),
    path("eliminar_cuenta/", EliminarCuentaView.as_view(), name='eliminar_cuenta'),
]
