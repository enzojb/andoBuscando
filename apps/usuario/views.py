from apps.usuario.models import Usuario
from .forms import UsuarioForm, EditarPerfilForm, EditarContraseniaForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from .forms import UsuarioForm, EditarPerfilForm, EditarSoyAgenteForm, EditarContraseniaForm

class RegistroView(CreateView):
    model = Usuario
    form_class = UsuarioForm 
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login') 

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index') 
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, 'Registro exitoso, ya puede iniciar sesión con sus datos.')
        return super().form_valid(form)
    
class PerfilView(LoginRequiredMixin, UpdateView):
    model = Usuario
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

class SoyAgenteView(LoginRequiredMixin, UpdateView):
    model = Usuario
    form_class = EditarSoyAgenteForm 
    template_name = 'soy_agente.html'
    success_url = reverse_lazy('soy_agente')

    def get_object(self):
        return self.request.user
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user 
        return context

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Fuiste inscripto cómo agente exitosamente.')
        return super().form_valid(form)
    
class CambiarContraseniaView(LoginRequiredMixin, UpdateView):
    model = Usuario
    form_class = EditarContraseniaForm
    template_name = 'change_password.html'
    success_url = reverse_lazy('cambiar_contrasenia')
    
    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        user = self.request.user
        user.set_password(form.cleaned_data['password'])
        user.save()
        update_session_auth_hash(self.request, user)
        messages.success(self.request, 'Tu contraseña ha sido cambiada exitosamente.')
        return super().form_valid(form)

class EliminarCuentaView(LoginRequiredMixin, DeleteView):
    template_name = 'delete_account.html'
    success_url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        return self.render_to_response({})

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')

        user = request.user

        user.delete()

        messages.success(request, "Tu cuenta ha sido eliminada exitosamente.")

        logout(request)

        return redirect(self.success_url)