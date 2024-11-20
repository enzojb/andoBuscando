from typing import Any
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView, ListView, FormView
from apps.propiedad.models import Propiedad
from apps.propiedad.forms import CrearPropiedadForm, EditarPropiedadForm
from django.contrib import messages
from django.conf import settings
from PIL import Image
import io
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class PropiedadView(ListView):
    model = Propiedad
    template_name = 'propiedades.html'
    context_object_name = 'propiedades'
    paginate_by = 8  # Paginación de 10 resultados por página


    def get_queryset(self):
        # Obtener las propiedades filtradas
        queryset = Propiedad.objects.all()  # Comienza con todas las propiedades

        # Obtener los parámetros de la URL (GET)
        tipo_propiedad = self.request.GET.get('tipo_propiedad')
        localidad = self.request.GET.get('localidad')
        tipo_operacion = self.request.GET.get('tipo_operacion')
        moneda = self.request.GET.get('moneda')
        min_precio = self.request.GET.get('min_precio')
        max_precio = self.request.GET.get('max_precio')
        min_metros_cuadrados = self.request.GET.get('metros_cuadrados')
        min_ambientes = self.request.GET.get('ambientes')

        # Filtrar según los parámetros disponibles
        if tipo_propiedad:
            queryset = queryset.filter(tipo_propiedad=tipo_propiedad)
        if localidad:
            queryset = queryset.filter(localidad=localidad)
        if tipo_operacion:
            queryset = queryset.filter(tipo_operacion=tipo_operacion)
        if moneda:
            queryset = queryset.filter(moneda__icontains=moneda)
        if min_precio:
            queryset = queryset.filter(precio__gte=min_precio)
        if max_precio:
            queryset = queryset.filter(precio__lte=max_precio)
        if min_metros_cuadrados:
            min_metros_cuadrados = min_metros_cuadrados.strip('[]').split(',')
            if len(min_metros_cuadrados) == 2:
                min_metros = int(min_metros_cuadrados[0])
                max_metros = int(min_metros_cuadrados[1])
                queryset = queryset.filter(metros_cuadrados__gte=min_metros, metros_cuadrados__lte=max_metros)
        if min_ambientes:
            min_ambientes = min_ambientes.strip('[]').split(',')
            if len(min_ambientes) == 2:
                min_amb = int(min_ambientes[0])
                max_amb = int(min_ambientes[1])
                queryset = queryset.filter(ambientes__gte=min_amb, ambientes__lte=max_amb)

            # Ordenar según los parámetros 'orderby' y 'order' si existen
        order_by = self.request.GET.get('orderby', 'fecha_creacion')  # por defecto por fecha de creación
        order = self.request.GET.get('order', 'ASC')  # por defecto en orden ascendente

        if order == 'ASC':
            queryset = queryset.order_by(order_by)
        else:
            queryset = queryset.order_by(f'-{order_by}')

        return queryset



class CrearPropiedadView(CreateView):
    model = Propiedad
    form_class = CrearPropiedadForm 
    template_name = 'carga_propiedad.html'
    success_url = reverse_lazy('propiedades') 
    def dispatch(self, request, *args, **kwargs):
        # Verificar si el usuario es un agente
        if not request.user.is_agente:
            messages.error(request, "Solo los agentes pueden crear propiedades.")
            return redirect('propiedades')  # Redirige a la lista de propiedades si no tiene permiso

        return super().dispatch(request, *args, **kwargs)
    def form_valid(self, form):
        form.instance.agente = self.request.user
        messages.success(self.request, 'Se cargo la propiedad, ya puede visualizarlo.')
        propiedad = form.save(commit=False)
        imagen = self.request.FILES.get('foto') 

        # Procesar la imagen con Pillow si existe
        if imagen:
            with Image.open(imagen) as img:
                img = img.convert('RGB')  # Asegúrate de que la imagen esté en RGB
                img.thumbnail((1500, 800))  # Redimensionar la imagen

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

class PropiedadDetalleView(DetailView):
    model = Propiedad
    template_name = "detalle_propiedad.html"
    context_object_name = 'propiedad'
    

class PropieadadActualizarView(LoginRequiredMixin,UpdateView):
    model = Propiedad
    form_class = EditarPropiedadForm
    template_name = "editar_propiedad.html"
    success_url = reverse_lazy('mis_propiedades')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Actualizaste la informacion de tu propiedad correctamente.')
        return super().form_valid(form)
    
    def dispatch(self, request, *args, **kwargs):
        propiedad = self.get_object()

        # Verifica si el usuario tiene permisos para editar la propiedad
        if not request.user.is_agente:  # Verifica si es un agente
            messages.error(request, "Solo los agentes pueden editar propiedades.")
            return redirect('/')  # Redirige a la lista de propiedades si no es un agente

        # Verifica si el agente que está editando la propiedad es el mismo que la creo
        if propiedad.agente != request.user:
            messages.error(request, "No tienes permiso para editar esta propiedad.")
            return redirect('/')  # Redirige a la lista de propiedades si no tiene permiso

        # Si el usuario tiene permisos, continúa con el flujo normal
        return super().dispatch(request, *args, **kwargs)
            
class EliminarPropiedadView(DeleteView):
    model = Propiedad
    template_name = "eliminar_propiedad.html"
    success_url = reverse_lazy('mis_propiedades')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["propiedades"] = Propiedad.objects.all()
        return context


    def dispatch(self, request, *args, **kwargs):
        propiedad = self.get_object()


        if not request.user.is_agente:  
            messages.error(request, "Solo los agentes pueden eliminar propiedades.")
            return redirect('/')  


        if propiedad.agente != request.user:
            messages.error(request, "No tienes permiso para eliminar esta propiedad.")
            return redirect('/') 

 
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        messages.success(request, "La propiedad ha sido eliminada exitosamente.")
        return super().delete(request, *args, **kwargs)


class ContactarAgenteView(LoginRequiredMixin,TemplateView):
    template_name = 'contactar_agente.html'
    login_url = "/login/"
    redirect_field_name = "redirect_to"
    raise_exception = False

    def get(self,request):
        return self.render_to_response({})
    
class MisPropiedadesView(ListView, LoginRequiredMixin):
    model = Propiedad
    template_name = "mis_propiedades.html"
    context_object_name = 'propiedades'
    def get_queryset(self):
        return Propiedad.objects.filter(agente=self.request.user)
    
    def dispatch(self, request, *args, **kwargs):

        if not request.user.is_agente:
            messages.error(request, "No tienes permiso para acceder a mis propiedades.")
            return redirect('/')  
        

        return super().dispatch(request, *args, **kwargs)
    
    
