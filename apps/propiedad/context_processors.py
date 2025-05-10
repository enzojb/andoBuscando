from .models import Propiedad

def ultimas_propiedades(request):
    return {
        'ultimas_propiedades': Propiedad.objects.order_by('-fecha_creacion')[:3]
    }