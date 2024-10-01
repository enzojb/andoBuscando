from django.db import models
from apps.agente.models import Agente
from apps.busqueda.models import Busqueda

class Agente_busqueda(models.Model):
    id = models.AutoField(primary_key=True)
    agente = models.OneToOneField(Agente, on_delete=models.CASCADE)
    busqueda = models.OneToOneField(Busqueda, on_delete=models.CASCADE)
