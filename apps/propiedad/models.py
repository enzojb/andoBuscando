from django.db import models

class Propiedad(models.Model):
    localidad = models.ForeignKey('propiedad.Localidad', on_delete=models.CASCADE)
    agente = models.ForeignKey('agente.Agente', on_delete=models.CASCADE)
    tipo_propiedad = models.ForeignKey('propiedad.TipoPropiedad', on_delete=models.CASCADE)
    ambientes = models.CharField(max_length=2)
    metros_cuadrados = models.CharField(max_length=4)
    precio = models.CharField(max_length=15)
    moneda = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=255)

class TipoOperacion(models.Model):
    tipo_operacion = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.tipo_operacion

class TipoPropiedad(models.Model):
    tipo_propiedad = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.tipo_propiedad
class PropiedadFoto(models.Model):
    propiedad = models.ForeignKey(Propiedad, on_delete=models.CASCADE)
    ubicacion_url = models.CharField(max_length=255)
    descripcion_foto = models.CharField(max_length=255)

class Localidad(models.Model):
    localidad = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.localidad