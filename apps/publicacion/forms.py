from django import forms
from apps.publicacion.models import Publicacion

# Creamos un formulario basado en el modelo Publicacion, que será utilizado en views.py 
# para manejar los datos de las publicaciones.
class CargarPublicacionForm(forms.ModelForm):
    # La clase Meta se utiliza para especificar el modelo sobre el que trabaja el formulario
    #  y los campos que se incluirán en el formulario.
    class Meta:
        # Definimos el modelo Publicacion y especificamos los campos del modelo que se incluirán
        #  en el formulario
        model = Publicacion
        fields = ['titulo', 'moneda', 'ambientes', 'descripcion', 'localidad', 'tipo_propiedad', 'tipo_operacion', 'precio']
#DASd
# Esta clase hereda de ModelForm, lo que genera automáticamente un formulario HTML basado en el 
# modelo Publicacion. Podemos renderizar el formulario en un template HTML utilizando 
# {{ form.as_p }}, lo que lo presentará en formato de párrafos.

class EditarPublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['titulo', 'moneda', 'ambientes', 'descripcion', 'localidad', 'tipo_propiedad', 'tipo_operacion', 'precio']
