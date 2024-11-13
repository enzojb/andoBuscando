from django.urls import path
from apps.propiedad.views import PropiedadView

urlpatterns=[
    path("",PropiedadView.as_view(), name="propiedades")
]