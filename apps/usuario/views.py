from django.views.generic import TemplateView
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import ClienteForm
from apps.usuario.models import Cliente

class RegistroView(TemplateView):
    template_name = 'registration/register.html'

class RegistroClienteView(CreateView):
    model = Cliente
    form_class = ClienteForm 
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login') 

    def form_valid(self, form):
        """Este método se llama cuando el formulario es válido"""
        messages.success(self.request, 'Registro exitoso, ya puede iniciar sesión con sus datos.')
        return super().form_valid(form)
