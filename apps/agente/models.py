from django.db import models

from core.models import UsuarioModelo

class Agente(UsuarioModelo):
    matricula = models.CharField(max_length=20)
    dni = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.nombre} {self.apellido} {self.matricula}'

class AgenteBusqueda(models.Model):
    agente = models.ForeignKey(Agente, on_delete=models.CASCADE)
    busqueda = models.ForeignKey('publicacion.Publicacion', on_delete=models.CASCADE)