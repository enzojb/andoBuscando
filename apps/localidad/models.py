from django.db import models

class Localidad(models.Model):
    id = models.AutoField(primary_key=True)
    localidad = models.CharField(max_length=100)