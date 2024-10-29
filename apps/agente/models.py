from django.db import models

from core.models import UsuarioModelo

class Agente(UsuarioModelo):
    matricula = models.CharField(max_length=20)
    dni = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)