from django.db import models
from apps.busqueda.models import Busqueda
from apps.tipo_operacion.models import TipoOperacion

class BusquedaTipoOper(models.Model):
    id = models.AutoField(primary_key=True)
    busqueda = models.OneToOneField(Busqueda, on_delete=models.CASCADE)
    tipo_operacion = models.OneToOneField(TipoOperacion, on_delete=models.CASCADE)