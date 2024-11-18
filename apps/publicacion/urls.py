from django.urls import path
from apps.publicacion.views import PublicacionListView, DashboardView, PublicacionCargaView, ContactarUsuarioView, PublicacionEdicionView, PublicacionEliminacionView
from . import views

urlpatterns=[
    path("busquedas/", PublicacionListView.as_view(), name="busquedas"),
    path("acciones_usuario/", DashboardView.as_view(), name="acciones_usuario"),
    path("cargar_publicacion/", PublicacionCargaView.as_view(), name="cargar_publicacion"),
    path("contactar_usuario/", ContactarUsuarioView.as_view() , name="contactar_usuario"),
    path("editar_publicacion/<int:pk>/", PublicacionEdicionView.as_view(),name="editar_publicacion"),
    path("eliminar_publicacion/<int:pk>/", PublicacionEliminacionView.as_view(), name="eliminar_publicacion")
]