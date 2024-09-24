from django.db import models

# Create your models here.
class Cliente(models.Model):
    name = models.CharField(max_length=255)
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100)
    contraseña = models.CharField(max_length=255)
    dni = models.CharField(max_length=10)
    telefono = models.CharField(max_length=15)
