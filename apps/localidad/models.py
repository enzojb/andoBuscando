from django.db import models

class Localidad(models.Model):
    localidad = models.CharField(max_length=100)