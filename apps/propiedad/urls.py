from django.urls import path
from apps.propiedad.views import PropiedadView, PropiedadDetalleView, CrearPropiedadView, ContactarAgenteView, PropieadadActualizarView, EliminarPropiedadView, MisPropiedadesView
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns=[
    path("",PropiedadView.as_view(), name="propiedades"),
    path("cargar_propiedad/",CrearPropiedadView.as_view(), name="cargar_propiedad"),
    path("detalles_propiedad/<int:pk>/",PropiedadDetalleView.as_view(), name="detalles_propiedad"),
    path("contactar_agente", ContactarAgenteView.as_view() , name="contactar_agente"),
    path("editar_propiedad/<int:pk>",PropieadadActualizarView.as_view(), name="editar_propiedad" ),
    path("eliminar_propiedad/<int:pk>",EliminarPropiedadView.as_view(), name="eliminar_propiedad" ),
    path("mis_propiedades/",MisPropiedadesView.as_view(), name="mis_propiedades" ),
    path('api/barrios/', views.obtener_barrios, name='obtener_barrios'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)