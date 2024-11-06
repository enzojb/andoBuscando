from django.db import models

class Publicacion(models.Model):
    cliente = models.ForeignKey('cliente.Cliente', on_delete=models.CASCADE)
    localidad = models.ForeignKey('propiedad.Localidad', on_delete=models.CASCADE)
    tipo_propiedad = models.ForeignKey('propiedad.TipoPropiedad', on_delete=models.CASCADE)
    tipo_operacion = models.ForeignKey('propiedad.TipoOperacion', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=40)
    ambientes = models.CharField(max_length=2)
    precio = models.CharField(max_length=15)
    moneda = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=255)

class PublicacionTipoOper(models.Model):
    busqueda = models.ForeignKey(Publicacion, on_delete=models.CASCADE)
    tipo_operacion = models.ForeignKey('propiedad.TipoOperacion', on_delete=models.CASCADE)

class PublicacionTipoProp(models.Model):
    busqueda =  models.ForeignKey(Publicacion, on_delete=models.CASCADE)
    tipo_propiedad =  models.ForeignKey('propiedad.TipoPropiedad', on_delete=models.CASCADE)

