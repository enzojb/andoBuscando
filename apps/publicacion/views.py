from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView # Importamos CreateView
from apps.publicacion.models import Publicacion
from apps.publicacion.forms import CargarPublicacionForm, EditarPublicacionForm # Importamos el formulario CargarPublicacionForm que se utiliza para crear publicaciones.
from django.urls import reverse_lazy # Importamos del modelo de urls el método de redirección
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.shortcuts import Http404, get_object_or_404

# Esta clase se encarga de renderizar la vista lista_publicaciones.html, mostrando todas las publicaciones existentes
#  en la base de datos.
class PublicacionView(TemplateView):
    template_name = "lista_publicaciones.html"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["publicaciones"] = Publicacion.objects.all()
        return context

# Codigo anterior:    
# class PublicacionCargaView(TemplateView):
#     template_name = "carga_publicacion.html"

#     def get_context_data(self, **kwargs: Any):
#         context = super().get_context_data(**kwargs)
#         context["cargar_publicacion"] = Publicacion.objects.all()
#         return context
#S
# Codigo nuevo:
# Esta clase se encarga de crear un nuevo registro de publicación en la base de datos.
#  Utiliza CreateView para facilitar la creación y validación del formulario.
# Lo que permite gestionar automáticamente la creación de una nueva publicación. 
# CreateView se encarga de mostrar el formulario, validarlo y guardarlo en la base de datos si los datos son válidos.
class PublicacionCargaView(CreateView):
    # Le indicamos:
    # model: el modelo sobre el que trabajará (en este caso, Publicacion).
    model = Publicacion
    # el formulario que se utilizará para capturar los datos (en este caso, CargarPublicacionForm)
    form_class = CargarPublicacionForm
    # la plantilla HTML donde se renderizará el formulario.
    template_name = 'carga_publicacion.html'
    # la URL a la que se redirigirá al usuario después de enviar correctamente el formulario."
    success_url = reverse_lazy('busquedas')  

# El método form_valid se llama cuando el formulario pasa todas las validaciones. 
# Aquí, asignamos el usuario autenticado (logueado) al campo cliente de la publicación antes de guardar la instancia.
# De manera similar, si el modelo Propiedad tiene un campo para asociar un agente (todavia cliente, no tenemos agentes),
#  también podríamos asignar ese campo utilizando form.instance.cliente(*) = self.request.user.cliente(*). (*)user.agente sería en el futuro
    def form_valid(self, form):
        # Asigna el cliente logueado al campo 'cliente' de la publicación
        form.instance.cliente = self.request.user.cliente  # El cliente está relacionado con el usuario logueado
        return super().form_valid(form)
    
class ContactarUsuarioView(LoginRequiredMixin,TemplateView):
    template_name = 'contactar_usuario.html'
    login_url = "/login/"
    redirect_field_name = "redirect_to"
    raise_exception = False

    def get(self,request):
        return self.render_to_response({})
    
class PublicacionLecturaView(ListView):
    model = Publicacion
    template_name = 'acciones_usuario.html'
    context_object_name = 'publicaciones'

    def get_queryset(self):
        return Publicacion.objects.filter(cliente=self.request.user.cliente)

class PublicacionView(TemplateView):
    template_name = 'editar_publicacion.html'

class PublicacionEdicionView(UpdateView):
    model = Publicacion
    form_class = EditarPublicacionForm
    template_name = 'editar_publicacion.html'
    success_url = reverse_lazy('publicacion')

    def get_object(self):
        try:
            publicacion = Publicacion.objects.get(pk=self.kwargs['pk'], cliente=self.request.user.cliente)
        except Publicacion.DoesNotExist:
            messages.error(self.request, 'Publicación no encontrada.')
            raise Http404("Publicación no encontrada")
        return publicacion
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Tu publicación se editó exitosamente.')
        return super().form_valid(form)
    
class PublicacionEliminacionView(DeleteView):
    model = Publicacion
    template_name = 'eliminar_publicación.html'
    success_url = reverse_lazy ('publicacion')

    def get_object(self):
        publicacion = get_object_or_404(Publicacion, pk=self.kwargs['pk'], cliente=self.request.user.cliente)
        return publicacion
    
    def delete(self, request, *args, **kwargs):
        publicacion = self.get_object()
        publicacion.delete()
        messages.success(request, 'La publicación ha sido eliminada exitosamente.')
        return redirect(self.success_url)