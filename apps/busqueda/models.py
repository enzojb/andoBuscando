from django.db import models
from apps.cliente.models import Cliente
from apps.localidad.models import Localidad

class Busqueda(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)
    localidad = models.OneToOneField(Localidad, on_delete=models.CASCADE)
    ambientes = models.CharField(max_length=10)
    dormitorios = models.CharField(max_length=10)
    banios = models.CharField(max_length=10)
    amenities = models.CharField(max_length=10)
    cochera = models.CharField(max_length=10)
    metros_cuadrados = models.CharField(max_length=10)
    precio = models.CharField(max_length=10)
    moneda = models.CharField(max_length=10)