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

class PublicacionView(TemplateView):
    template_name = "lista_publicaciones.html"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["publicaciones"] = Publicacion.objects.all()
        return context

class PublicacionCargaView(CreateView):
    model = Publicacion
    form_class = CargarPublicacionForm
    template_name = 'carga_publicacion.html'
    success_url = reverse_lazy('busquedas')  

    def form_valid(self, form):
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