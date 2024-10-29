from django.db import models

class TipoPropiedad(models.Model):
    tipo_propiedad = models.CharField(max_length=100)