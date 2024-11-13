from django.urls import path
from apps.publicacion.views import PublicacionView

urlpatterns=[
    path("busquedas/",PublicacionView.as_view(), name="busquedas")
]