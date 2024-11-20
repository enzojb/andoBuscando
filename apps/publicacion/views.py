from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView # Importamos CreateView
from apps.publicacion.models import Publicacion
from apps.publicacion.forms import CargarPublicacionForm, EditarPublicacionForm # Importamos el formulario CargarPublicacionForm que se utiliza para crear publicaciones.
from django.urls import reverse_lazy # Importamos del modelo de urls el método de redirección
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.shortcuts import Http404, get_object_or_404

# Vista para listar publicaciones hechas por cualquier usuario
class PublicacionListView(ListView):
    model = Publicacion
    template_name = "lista_publicaciones.html"
    context_object_name = "publicaciones"
    paginated_by = 8

    def get_queryset(self):
        queryset = Publicacion.objects.all()

        localidad = self.request.GET.get('localidad')
        tipo_operacion = self.request.GET.get('tipo_operacion')
        min_precio = self.request.GET.get('min_precio')
        max_precio = self.request.GET.get('max_precio')
        ambientes = self.request.GET.get('ambientes')

        if localidad:
            queryset = queryset.filter(localidad=localidad)
        if tipo_operacion:
            queryset = queryset.filter(tipo_operacion=tipo_operacion)
        if min_precio:
            queryset = queryset.filter(precio__gte=min_precio)
        if max_precio:
            queryset = queryset.filter(precio__lte=max_precio)
       
                
        order_by = self.request.GET.get('orderby', 'fecha_creacion')
        order = self.request.GET.get('order', 'ASC')

        if order == 'ASC':
            queryset = queryset.order_by(order_by)
        else:
            queryset = queryset.order_by(f'-{order_by}')

        return queryset
        
# Vista de acciones usuario
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "acciones_usuario.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['publicaciones'] = Publicacion.objects.filter(cliente=self.request.user)
        return context

# Vista para cargar busquedas
class PublicacionCargaView(CreateView):
    model = Publicacion
    form_class = CargarPublicacionForm
    template_name = 'carga_publicacion.html'
    success_url = reverse_lazy('acciones_usuario')  

    def form_valid(self, form):
        form.instance.cliente = self.request.user
        return super().form_valid(form)
    
# Vista para el "chat de contacto"    
class ContactarUsuarioView(LoginRequiredMixin,TemplateView):
    template_name = 'contactar_usuario.html'
    login_url = "/login/"
    redirect_field_name = "redirect_to"
    raise_exception = False

    def get(self,request):
        return self.render_to_response({})
    
# Vista para editar publicaciones
class PublicacionEdicionView(UpdateView):
    model = Publicacion
    form_class = EditarPublicacionForm
    template_name = 'editar_publicacion.html'
    success_url = reverse_lazy('acciones_usuario')

    def get_object(self):
        try:
            publicacion = Publicacion.objects.get(pk=self.kwargs['pk'], cliente=self.request.user)
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

# Vista para eliminar publicaciones  
class PublicacionEliminacionView(DeleteView):
    model = Publicacion
    template_name='eliminar_publicacion.html'
    success_url = reverse_lazy ('acciones_usuario')

    def get_object(self):
        publicacion = get_object_or_404(Publicacion, pk=self.kwargs['pk'], cliente=self.request.user)
        return publicacion
    
    def delete(self, request, *args, **kwargs):
        publicacion = self.get_object()
        publicacion.delete()
        messages.success(request, 'La publicación ha sido eliminada exitosamente.')
        return redirect(self.success_url)

