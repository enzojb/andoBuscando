from django.db import models
from apps.propiedad.models import Propiedad

class Propiedad_foto(models.Model):
    id = models.AutoField(primary_key=True)
    propiedad = models.ForeignKey(Propiedad, on_delete=models.CASCADE)
    ubicacion_url = models.CharField(max_length=255)
    descripcion_foto = models.CharField(max_length=255)
