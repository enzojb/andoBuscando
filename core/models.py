from django.db import models

class UsuarioModelo(models.Model):
    class Meta:
        abstract = True

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100)
    contraseña = models.CharField(max_length=255)