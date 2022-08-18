from django import forms
from django.core import validators

from .models import Horarios

class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'

class RegisterForm(forms.ModelForm):
    nombre = forms.CharField(label='Nombre Clase',widget= forms.TextInput(attrs={'class':'form-control','placeholder': 'Nombre clase'}))
    Fecha = forms.DateField(label='Fecha clase',widget= forms.DateInput(attrs={'type': 'date','class':'form-control'}))
    #personas = forms.CharField(label='Nombre Clase',widget= forms.TextInput(attrs={'class':'form-control','placeholder': 'Nombre clase'}))
    
    class Meta:
        model = Horarios
        fields = ['nombre','Fecha']
        exclude = ['personas']
        
