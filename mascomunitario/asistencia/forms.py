from django import forms
from django.core import validators

from .models import Horarios

estados_curso = [
    ('Encuentro Grupal', 'Encuentro Grupal'),
    ('Encuentro Situado', 'Encuentro Situado'),
    ('Bitacora', 'Bitacora'),
    ('Entrega de OVA', 'Entrega de OVA'),
]

class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'


class RegisterForm(forms.ModelForm):
    nombre = forms.ChoiceField(label='Nombre Clase', choices=estados_curso, widget= forms.Select(attrs={'class':'select2 form-select'}))
    Fecha = forms.DateField(label='Fecha clase', widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    #  personas = forms.CharField(label='Nombre Clase',widget= forms.TextInput(attrs={'class':'form-control','placeholder': 'Nombre clase'}))

    class Meta:
        model = Horarios
        fields = ['nombre', 'Fecha']
        exclude = ['personas']
