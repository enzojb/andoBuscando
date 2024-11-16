from typing import Any
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from apps.propiedad.models import Propiedad
from apps.propiedad.forms import CrearPropiedadForm
import os
from django.conf import settings
from PIL import Image
import io
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class PropiedadView(TemplateView):
    template_name = "lista_propiedades.html"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["propiedades"] = Propiedad.objects.all()
        return context



class CrearPropiedadView(CreateView):
    model = Propiedad
    form_class = CrearPropiedadForm 
    template_name = 'carga_propiedad.html'
    success_url = reverse_lazy('propiedades') 
    def form_valid(self, form):
        # Guardar el objeto sin confirmar
        propiedad = form.save(commit=False)
        imagen = self.request.FILES.get('foto')  # Cambia 'foto' según el nombre del campo

        # Procesar la imagen con Pillow si existe
        if imagen:
            with Image.open(imagen) as img:
                img = img.convert('RGB')  # Asegúrate de que la imagen esté en RGB
                img.thumbnail((800, 800))  # Redimensionar la imagen

                # Guardar la imagen en memoria
                buffer = io.BytesIO()
                img.save(buffer, format='JPEG')  # Cambia el formato si es necesario
                buffer.seek(0)

                # Crear un nuevo archivo cargado en memoria
                propiedad.foto = InMemoryUploadedFile(
                    buffer,  # Archivo en memoria
                    'ImageField',  # Campo relacionado
                    imagen.name,  # Nombre original del archivo
                    'image/jpeg',  # Tipo MIME
                    buffer.getbuffer().nbytes,  # Tamaño del archivo
                    None  # Opcional: Charset
                )

        propiedad.save()  # Guardar el modelo con la imagen procesada
        return super().form_valid(form)

class PropiedadDetalleView(TemplateView):
    template_name = "detalle_propiedad.html"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["detalles_propiedad"] = Propiedad.objects.all()
        return context

class ContactarAgenteView(LoginRequiredMixin,TemplateView):
    template_name = 'contactar_agente.html'
    login_url = "/signup/"
    redirect_field_name = "redirect_to"
    raise_exception = True

    def get(self,request):
        return self.render_to_response({})