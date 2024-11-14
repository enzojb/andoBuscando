from django.urls import path
from apps.usuario.views import RegistroView, RegistroClienteView, PerfilView, EditarPerfilView, CambiarContraseniaView, EditarContraseniaView

urlpatterns = [
    path("registro/", RegistroView.as_view(), name='registro'),
    path("registro_cliente/", RegistroClienteView.as_view(), name='registro_cliente'),
    path("perfil/", PerfilView.as_view(), name='perfil'),
    path("editar_perfil/", EditarPerfilView.as_view(), name='editar_perfil'),
    path("cambiar_contrasenia/", CambiarContraseniaView.as_view(), name='cambiar_contrasenia'),
    path("editar_contrasenia/", EditarContraseniaView.as_view(), name='editar_contrasenia'),
]
