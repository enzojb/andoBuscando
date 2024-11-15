from django import forms
from apps.propiedad.models import Propiedad


class CrearPropiedadForm(forms.ModelForm):
    class Meta:
        model = Propiedad
        fields = ['titulo','moneda','precio','tipo_operacion','descripcion','localidad','direccion','tipo_propiedad','ambientes','metros_cuadrados']
