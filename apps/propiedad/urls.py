from django.urls import path
from apps.propiedad.views import PropiedadView, PropiedadCargaView

urlpatterns=[
    path("",PropiedadView.as_view(), name="propiedades"),
    path("cargarpropiedad/",PropiedadCargaView.as_view(), name="carga propiedades")
]