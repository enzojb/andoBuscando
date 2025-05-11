from django.shortcuts import render
from django.http import JsonResponse
from apps.propiedad.models import Propiedad
from apps.publicacion.models import Publicacion
from apps.usuario.models import Usuario

def contador_datos(request):
    data = {
        'usuarios': Usuario.objects.count(),
        'propiedades': Propiedad.objects.count(),
        'publicaciones': Publicacion.objects.count(),
    }
    return JsonResponse(data)
