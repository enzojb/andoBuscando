from django.db import models
from apps.propiedad_agente.models import Propiedad_agente

class Propiedad_foto(models.Model):
    id = models.AutoField(primary_key=True)
    propiedad = models.OneToOneField(Propiedad_agente, on_delete=models.CASCADE)
    ubicacion_url = models.CharField(max_length=255)
    descripcion_foto = models.CharField(max_length=255)
# Create your models here.
