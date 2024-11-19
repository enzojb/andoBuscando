from django import forms
from apps.publicacion.models import Publicacion
from decimal import Decimal

class CargarPublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['titulo', 'moneda', 'ambientes', 'descripcion', 'localidad', 'tipo_propiedad', 'tipo_operacion', 'precio']

# Si la única diferencia entre crear y editar una publicación es cómo manejas la instancia 
# del modelo en la vista, puedes unificar ambos formularios en un solo formulario PublicacionForm.
class EditarPublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['titulo', 'moneda', 'ambientes', 'descripcion', 'localidad', 'tipo_propiedad', 'tipo_operacion', 'precio']
    