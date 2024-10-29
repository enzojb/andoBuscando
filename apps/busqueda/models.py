from django.db import models

class Busqueda(models.Model):
    cliente = models.ForeignKey('cliente.Cliente', on_delete=models.CASCADE)
    localidad = models.ForeignKey('localidad.Localidad', on_delete=models.CASCADE)
    tipo_propiedad = models.ForeignKey('tipo_propiedad.TipoPropiedad', on_delete=models.CASCADE)
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