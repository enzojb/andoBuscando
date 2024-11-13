from django.urls import path
from apps.usuario.views import RegistroView, RegistroClienteView

urlpatterns = [
    path("registro/", RegistroView.as_view(), name='registro'),
    path("registro_cliente/", RegistroClienteView.as_view(), name='registro_cliente'),
]
