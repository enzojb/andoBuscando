from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from apps.propiedad.models import Propiedad

# Create your views here.
class PropiedadView(TemplateView):
    template_name = "lista_propiedades.html"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["propiedades"] = Propiedad.objects.all()
        return context

class PropiedadCargaView(TemplateView):
    template_name = "carga_propiedad.html"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["cargar_propiedad"] = Propiedad.objects.all()
        return context
    