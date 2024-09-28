from django.db import models

class TipoOperacion(models.Model):
    id = models.AutoField(primary_key=True)
    tipo_operacion = models.CharField(max_length=100)