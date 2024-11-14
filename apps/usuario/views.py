from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from .forms import ClienteForm, EditarPerfilForm, EditarContraseniaForm
from apps.usuario.models import Cliente

class RegistroView(TemplateView):
    template_name = 'registration/register.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        return super().get(request, *args, **kwargs)

class RegistroClienteView(CreateView):
    model = Cliente
    form_class = ClienteForm 
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login') 

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index') 
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, 'Registro exitoso, ya puede iniciar sesión con sus datos.')
        return super().form_valid(form)

class PerfilView(TemplateView):
    template_name = 'profile.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('index')
        return super().get(request, *args, **kwargs)
    
class EditarPerfilView(UpdateView):
    model = Cliente
    form_class = EditarPerfilForm 
    template_name = 'profile.html'
    success_url = reverse_lazy('perfil')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index') 
        return super().get(request, *args, **kwargs)

    def get_object(self):
        return self.request.user
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user 
        return context

    def form_valid(self, form):
        form.instance = self.request.user
        form.save()
        messages.success(self.request, 'Tu perfil ha sido actualizado exitosamente.')
        return super().form_valid(form)
    
class CambiarContraseniaView(TemplateView):
    template_name = 'change_password.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('index')
        return super().get(request, *args, **kwargs)
    
class EditarContraseniaView(UpdateView):
    model = Cliente
    form_class = EditarContraseniaForm
    template_name = 'change_password.html'
    success_url = reverse_lazy('cambiar_contrasenia')

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('index')
        return super().get(request, *args, **kwargs)
    
    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        user = self.request.user
        user.set_password(form.cleaned_data['password'])
        user.save()
        update_session_auth_hash(self.request, user)
        messages.success(self.request, 'Tu contraseña ha sido cambiada exitosamente.')
        return super().form_valid(form)