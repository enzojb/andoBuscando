from django.urls import path
from apps.propiedad.views import PropiedadView, PropiedadCargaView

urlpatterns=[
    path("",PropiedadView.as_view(), name="propiedades"),
    path("cargar_propiedad/",PropiedadCargaView.as_view(), name="cargar_propiedad")
]