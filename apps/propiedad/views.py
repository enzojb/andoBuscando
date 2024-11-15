from typing import Any
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from apps.propiedad.models import Propiedad
from apps.propiedad.forms import CrearPropiedadForm

class PropiedadView(TemplateView):
    template_name = "lista_propiedades.html"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["propiedades"] = Propiedad.objects.all()
        return context

"""class PropiedadCargaView(TemplateView):
    template_name = "carga_propiedad.html"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["cargar_propiedad"] = Propiedad.objects.all()
        return context """

class CrearPropiedadView(CreateView):
    model = Propiedad
    form_class = CrearPropiedadForm 
    template_name = 'carga_propiedad.html'
    success_url = reverse_lazy('propiedades') 

class PropiedadDetalleView(TemplateView):
    template_name = "detalle_propiedad.html"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["detalles_propiedad"] = Propiedad.objects.all()
        return context