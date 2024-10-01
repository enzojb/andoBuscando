from django.db import models
from apps.busqueda.models import Busqueda
from apps.tipo_propiedad.models import Tipo_Propiedad

class BusquedaTipoProp(models.Model):
    id = models.AutoField(primary_key=True)
    busqueda =  models.OneToOneField(Busqueda, on_delete=models.CASCADE)
    tipo_propiedad =  models.OneToOneField(Tipo_Propiedad, on_delete=models.CASCADE)