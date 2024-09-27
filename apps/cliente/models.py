from django.db import models
from apps.usuario.models import Usuario

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    dni = models.CharField(max_length=10)
    telefono = models.CharField(max_length=15)
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)