from django.db import models
from apps.cliente.models import Cliente
from apps.localidad.models import Localidad
from apps.tipo_propiedad.models import Tipo_Propiedad

class Busqueda(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    localidad = models.OneToOneField(Localidad, on_delete=models.CASCADE)
    tipo_propiedad = models.OneToOneField(Tipo_Propiedad, on_delete=models.CASCADE)
    ambientes = models.CharField(max_length=2)
    dormitorios = models.CharField(max_length=2)
    banios = models.CharField(max_length=2)
    amenities = models.CharField(max_length=255)
    cochera = models.CharField(max_length=2)
    metros_cuadrados = models.CharField(max_length=4)
    precio = models.CharField(max_length=15)
    moneda = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=255)