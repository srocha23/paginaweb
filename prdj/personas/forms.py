from django.forms import EmailInput, ModelForm, TextInput, FileInput
from personas.models import Persona , Domicilio , Producto , Categoria


class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        widgets = {
            'email': EmailInput(attrs={'type': 'email'})
        }

class DomicilioForm(ModelForm):
    class Meta:
        model = Domicilio
        fields = '__all__'
        widgets = {
            'pais': TextInput(attrs={'type': 'text'})
        }


class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'imagen': FileInput(attrs={'accept': 'image/*'})
        }

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'
        widgets = {
            'nombre': TextInput(attrs={'type': 'text'})
        }