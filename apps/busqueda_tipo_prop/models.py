from django.db import models
from apps.busqueda.models import Busqueda
from apps.tipo_propiedad.models import TipoPropiedad

class BusquedaTipoProp(models.Model):
    id = models.AutoField(primary_key=True)
    busqueda =  models.OneToOneField(Busqueda, on_delete=models.CASCADE)
    tipo_propiedad =  models.OneToOneField(TipoPropiedad, on_delete=models.CASCADE)