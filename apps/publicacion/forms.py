from django import forms
from apps.publicacion.models import Publicacion
from decimal import Decimal

class CargarPublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['titulo', 'moneda', 'ambientes', 'descripcion', 'localidad', 'tipo_propiedad', 'tipo_operacion', 'precio']

class EditarPublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['titulo', 'moneda', 'ambientes', 'descripcion', 'localidad', 'tipo_propiedad', 'tipo_operacion', 'precio']

class BuscarPublicacionesForm(forms.ModelForm):
    min_precio = forms.DecimalField(required=False, label="Precio mínimo")
    max_precio = forms.DecimalField(required=False, label="Precio máximo")

    class Meta:
        model = Publicacion
        fields = ['localidad', 'tipo_operacion', 'tipo_propiedad']
