from django.urls import path
from apps.propiedad.views import PropiedadView, PropiedadDetalleView, CrearPropiedadView

urlpatterns=[
    path("",PropiedadView.as_view(), name="propiedades"),
    path("cargar_propiedad/",CrearPropiedadView.as_view(), name="cargar_propiedad"),
    path("detalles_propiedad/",PropiedadDetalleView.as_view(), name="detalles_propiedad")
]