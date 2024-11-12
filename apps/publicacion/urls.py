from django.urls import path
from apps.publicacion.views import PublicacionView

urlpatterns=[
    path("",PublicacionView.as_view(), name="publicacion")
]