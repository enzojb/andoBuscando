from django import forms
from apps.propiedad.models import Propiedad


class CrearPropiedadForm(forms.ModelForm):
    class Meta:
        model = Propiedad
        fields = ['titulo','foto','moneda','precio','tipo_operacion','descripcion','localidad','direccion','tipo_propiedad','ambientes','metros_cuadrados']


class EditarPropiedadForm(forms.ModelForm):
    class Meta:
        model = Propiedad
        fields = ['titulo','foto','moneda','precio','tipo_operacion','descripcion','localidad','direccion','tipo_propiedad','ambientes','metros_cuadrados']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Hacer que los campos no sean obligatorios
        for field in self.fields:
            if self.instance and getattr(self.instance, field):
                self.fields[field].required = False
    
    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo')
        if not titulo:
            return self.instance.titulo  # Mantiene el valor
        return titulo

    def clean_foto(self):
        foto = self.cleaned_data.get('foto')
        if not foto:
            return self.instance.foto
        return foto
    
    def clean_moneda(self):
        moneda = self.cleaned_data.get('moneda')
        if not moneda:
            return self.instance.moneda 
        return moneda
    
    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if not precio:
            return self.instance.precio 
        return precio
    
    def clean_tipo_operacion(self):
        tipo_operacion = self.cleaned_data.get('tipo_operacion')
        if not tipo_operacion:
            return self.instance.tipo_operacion
        return tipo_operacion
    
    def clean_descripcion(self):
        descripcion = self.cleaned_data.get('descripcion')
        if not descripcion:
            return self.instance.descripcion
        return descripcion

    def clean_localidad(self):
        localidad = self.cleaned_data.get('localidad')
        if not localidad:
            return self.instance.localidad
        return localidad

    def clean_direccion(self):
        direccion = self.cleaned_data.get('direccion')
        if not direccion:
            return self.instance.direccion
        return direccion

    def clean_tipo_propiedad(self):
        tipo_propiedad = self.cleaned_data.get('tipo_propiedad')
        if not tipo_propiedad:
            return self.instance.tipo_propiedad
        return tipo_propiedad
    
    def clean_ambientes(self):
        ambientes = self.cleaned_data.get('ambientes')
        if not ambientes:
            return self.instance.ambientes
        return ambientes

    def clean_metros_cuadrados(self):
        metros_cuadrados = self.cleaned_data.get('metros_cuadrados')
        if not metros_cuadrados:
            return self.instance.metros_cuadrados
        return metros_cuadrados


class BuscarPropiedadForm(forms.ModelForm):
    min_precio = forms.DecimalField(required=False, label="Precio mínimo")
    max_precio = forms.DecimalField(required=False, label="Precio máximo")
    min_metros_cuadrados = forms.IntegerField(required=False, label="Mínimo m²")
    max_metros_cuadrados = forms.IntegerField(required=False, label="Máximo m²")
    min_ambientes = forms.IntegerField(required=False, label="Mínimo ambientes")
    max_ambientes = forms.IntegerField(required=False, label="Máximo ambientes")

    class Meta:
        model = Propiedad
        fields = ['localidad', 'tipo_operacion', 'moneda','tipo_propiedad' ]
        