from django.urls import path
from apps.propiedad.views import PropiedadView, PropiedadDetalleView, CrearPropiedadView, ContactarAgenteView
from django.conf.urls.static import static
from django.conf import settings
urlpatterns=[
    path("",PropiedadView.as_view(), name="propiedades"),
    path("cargar_propiedad/",CrearPropiedadView.as_view(), name="cargar_propiedad"),
    path("detalles_propiedad/<int:id>/",PropiedadDetalleView.as_view(), name="detalles_propiedad"),
    path("contactar_agente", ContactarAgenteView.as_view() , name="contactar_agente")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)