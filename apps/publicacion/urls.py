from django.urls import path
from apps.publicacion.views import PublicacionView, PublicacionCargaView

urlpatterns=[
    path("busquedas/", PublicacionView.as_view(), name="busquedas"),
    path("cargar_publicacion/", PublicacionCargaView.as_view(), name="cargar_publicacion")
]