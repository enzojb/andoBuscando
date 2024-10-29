from django.db import models

from core.models import UsuarioModelo

class Moderador(UsuarioModelo):
    pass

    def __str__(self):
        return f'{self.nombre} {self.apellido}'