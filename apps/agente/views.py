from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from apps.agente.models import Agente

# Create your views here.
class AgenteView(TemplateView):
    template_name = "lista_agente.html"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["agentes"] = Agente.objects.all()
        return context
    