from django.db import models

class Propiedad(models.Model):
    localidad = models.ForeignKey('propiedad.Localidad', on_delete=models.CASCADE)
    #agente = models.ForeignKey('usuario.Agente', on_delete=models.CASCADE)
    tipo_propiedad = models.ForeignKey('propiedad.TipoPropiedad', on_delete=models.CASCADE)
    tipo_operacion = models.ForeignKey('propiedad.TipoOperacion', on_delete=models.CASCADE, default='')
    titulo= models.CharField(max_length=50, default='sin titulo')
    foto = models.ImageField(upload_to='images', null=True, blank=True)
    ambientes = models.PositiveIntegerField()
    metros_cuadrados = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    moneda = models.CharField(max_length=30)
    direccion = models.CharField(max_length=55)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True) 

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
    ubicacion_url = models.URLField(max_length=255)
    descripcion_foto = models.CharField(max_length=255)

    def __str__(self):
        return f"Foto de {self.propiedad} - {self.descripcion_foto}"

class Localidad(models.Model):
    localidad = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.localidad