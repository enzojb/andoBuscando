from django.db import models

class BusquedaTipoOper(models.Model):
    busqueda = models.ForeignKey('busqueda.Busqueda', on_delete=models.CASCADE)
    tipo_operacion = models.ForeignKey('tipo_operacion.TipoOperacion', on_delete=models.CASCADE)