from django.urls import path
from apps.publicacion.views import PublicacionView, PublicacionCargaView, ContactarUsuarioView, PublicacionView, PublicacionEdicionView
from . import views

urlpatterns=[
    path("busquedas/", PublicacionView.as_view(), name="busquedas"),
    path("cargar_publicacion/", PublicacionCargaView.as_view(), name="cargar_publicacion"),
    path("contactar_usuario", ContactarUsuarioView.as_view() , name="contactar_usuario"),
    path("publicacion", PublicacionView.as_view(), name= "publicacion"),
    path("editar_publicacion", PublicacionEdicionView.as_view(),name="editar_publicacion")

]