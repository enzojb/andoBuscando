from django.db import models
from apps.usuario.models import Usuario

class Agente(models.Model):
    id = models.AutoField(primary_key=True)
    dni = models.CharField(max_length=10)
    telefono = models.CharField(max_length=15)
    matricula = models.CharField(max_length=10)
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
