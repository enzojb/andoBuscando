from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from apps.publicacion.models import Publicacion

class PublicacionView(TemplateView):
    template_name = "lista_publicaciones.html"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["publicaciones"] = Publicacion.objects.all()
        return context
    
class PublicacionCargaView(TemplateView):
    template_name = "carga_publicacion.html"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["cargar_publicacion"] = Publicacion.objects.all()
        return context
    