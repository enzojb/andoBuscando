from django.db import models

class TipoOperacion(models.Model):
    tipo_operacion = models.CharField(max_length=100)