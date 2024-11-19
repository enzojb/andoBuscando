from django.db import models

class Publicacion(models.Model):
    cliente = models.ForeignKey('usuario.Usuario', on_delete=models.CASCADE)
    localidad = models.ForeignKey('propiedad.Localidad', on_delete=models.CASCADE)
    tipo_propiedad = models.ForeignKey('propiedad.TipoPropiedad', on_delete=models.CASCADE)
    tipo_operacion = models.ForeignKey('propiedad.TipoOperacion', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=40)
    ambientes = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    moneda = models.CharField(max_length=30)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

class AgentePublicacion(models.Model):
    agente = models.ForeignKey('usuario.Usuario', on_delete=models.CASCADE)
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)    

    def __str__(self):
        return f"{self.agente} - {self.publicacion.titulo}"

class PublicacionTipoOper(models.Model):
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)
    tipo_operacion = models.ForeignKey('propiedad.TipoOperacion', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.publicacion.titulo} - {self.tipo_operacion}"

class PublicacionTipoProp(models.Model):
    publicacion =  models.ForeignKey(Publicacion, on_delete=models.CASCADE)
    tipo_propiedad =  models.ForeignKey('propiedad.TipoPropiedad', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.publicacion.titulo} - {self.tipo_propiedad}"