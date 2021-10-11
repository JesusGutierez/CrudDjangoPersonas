from django import forms
from .models import Persona
class PersonaForm(forms.ModelForm):
    class Meta:
        model=Persona # model alamcenara la clase  Persona
        fields='__all__' # all indica que se va a usar todos los campos de la clase Persona