from django.db import models

from core.models import UsuarioModelo

class Cliente(UsuarioModelo):
    dni = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.nombre} {self.apellido} {self.dni}'