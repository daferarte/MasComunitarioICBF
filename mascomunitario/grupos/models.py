from django.db import models
from mainapp.models import Personas

# Create your models here.
class Grupos(models.Model):
    nombre=models.CharField(max_length=100, verbose_name='Nombre')
    descripcion=models.CharField(max_length=150, verbose_name='Descripción')
    personas = models.ManyToManyField(Personas, verbose_name="Docentes", blank=True)
    create_at=models.DateTimeField(auto_now_add=True,verbose_name='Creado')
    update_at=models.DateTimeField(auto_now=True,verbose_name='Editado')

    class Meta:
        verbose_name='Grupo'
        verbose_name_plural='Grupos'
        
    def __str__(self):
        return str(self.nombre)