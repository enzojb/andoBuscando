from django.db import models
from apps.agente.models import Agente
from apps.propiedad_agente.models import Propiedad_agente

class Busqueda_prop(models.Model):
    id= models.AutoField(primary_key=True)
    agente = models.OneToOneField(Agente, on_delete=models.CASCADE)
    propiedad = models.OneToOneField(Propiedad_agente, on_delete=models.CASCADE)
# Create your models here.
