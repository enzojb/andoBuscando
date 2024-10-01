from django.db import models
from apps.usuario.models import Usuario

class Moderador(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)