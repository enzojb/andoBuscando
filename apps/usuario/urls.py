from django.urls import path
from apps.usuario.views import registro_cliente

urlpatterns = [
    path('', registro_cliente, name='registro_cliente'),
]
