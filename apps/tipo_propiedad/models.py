from django.db import models

class TipoPropiedad(models.Model):
    id = models.AutoField(primary_key=True)
    tipo_propiedad = models.CharField(max_length=100)