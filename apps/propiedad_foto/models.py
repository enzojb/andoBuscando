from django.db import models

class PropiedadFoto(models.Model):
    propiedad = models.ForeignKey('propiedad.Propiedad', on_delete=models.CASCADE)
    ubicacion_url = models.CharField(max_length=255)
    descripcion_foto = models.CharField(max_length=255)
