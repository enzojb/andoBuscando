from django.db import models

class BusquedaTipoProp(models.Model):
    busqueda =  models.ForeignKey('busqueda.Busqueda', on_delete=models.CASCADE)
    tipo_propiedad =  models.ForeignKey('tipo_propiedad.TipoPropiedad', on_delete=models.CASCADE)