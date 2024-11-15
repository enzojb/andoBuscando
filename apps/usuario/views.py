from apps.usuario.models import Cliente
from .forms import ClienteForm, EditarPerfilForm, EditarContraseniaForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash, logout
from django.contrib.auth.mixins import LoginRequiredMixin

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

class PerfilView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'
    
class EditarPerfilView(LoginRequiredMixin, UpdateView):
    model = Cliente
    form_class = EditarPerfilForm 
    template_name = 'profile.html'
    success_url = reverse_lazy('perfil')

    def get_object(self):
        return self.request.user
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user 
        return context

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Tu perfil ha sido actualizado exitosamente.')
        return super().form_valid(form)
    
class CambiarContraseniaView(LoginRequiredMixin, TemplateView):
    template_name = 'change_password.html'
    
class EditarContraseniaView(LoginRequiredMixin, UpdateView):
    model = Cliente
    form_class = EditarContraseniaForm
    template_name = 'change_password.html'
    success_url = reverse_lazy('cambiar_contrasenia')
    
    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        self.request.user.set_password(form.cleaned_data['password_current'])
        self.request.user.save()
        update_session_auth_hash(self.request, self.request.user)
        messages.success(self.request, 'Tu contraseña ha sido cambiada exitosamente.')
        return super().form_valid(form)

class EliminarCuentaView(LoginRequiredMixin, TemplateView):
    template_name = 'delete_account.html'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class ConfirmarEliminarCuentaView(LoginRequiredMixin, TemplateView):
    template_name = 'delete_account.html'

    def post(self, request, *args, **kwargs):
        user = request.user

        user.delete()

        logout(request)

        messages.success(request, 'Tu cuenta ha sido eliminada exitosamente.')
        return redirect(reverse_lazy('index'))