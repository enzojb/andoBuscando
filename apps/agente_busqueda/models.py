from django.db import models

class AgenteBusqueda(models.Model):
    agente = models.ForeignKey('agente.Agente', on_delete=models.CASCADE)
    busqueda = models.ForeignKey('busqueda.Busqueda', on_delete=models.CASCADE)
