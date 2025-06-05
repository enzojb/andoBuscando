"""
URL configuration for andoBuscando project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path("login/", auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path("logout/", auth_views.LogoutView.as_view(), name='logout'),
    path('usuario/', include('apps.usuario.urls'), name='usuario'),
    path('publicacion/', include('apps.publicacion.urls'), name='publicacion'),
    path('terminos/', include('apps.publicacion.urls'), name='terminos'),
    path('contacto/', include('apps.publicacion.urls'), name='contacto'),
    path('faq/', include('apps.publicacion.urls'), name='faq'),
    path('propiedad/', include('apps.propiedad.urls'), name='propiedad'),
    path('contador/', include('apps.contador.urls'), name='contador'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)