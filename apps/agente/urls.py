from django.urls import path
from apps.agente.views import AgenteView

urlpatterns=[
    path("",AgenteView.as_view(), name="agente")
]

