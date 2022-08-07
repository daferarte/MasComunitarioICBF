from django.db import models
from grupos.models import Grupos
from mainapp.models import Personas
# Create your models here.
class Listas(models.Model):
    cedula=models.CharField(max_length=50, verbose_name='Cedula')
    nombre=models.CharField(max_length=100, verbose_name='Nombre')
    Apellido=models.CharField(max_length=100, verbose_name='apellido')
    Grupo=models.ManyToManyField(Grupos, verbose_name="Grupo", blank=True)
    create_at=models.DateTimeField(auto_now_add=True,verbose_name='Creado')
    update_at=models.DateTimeField(auto_now=True,verbose_name='Editado')

    class Meta:
        verbose_name='Lista'
        verbose_name_plural='Listas'
        
    def __str__(self):
        return str(self.cedula)

class Horarios(models.Model):
    nombre=models.CharField(max_length=100, verbose_name='Numero clase')
    Fecha=models.DateTimeField(verbose_name='Fecha')
    personas = models.ManyToManyField(Personas, verbose_name="Docentes", blank=True)
    create_at=models.DateTimeField(auto_now_add=True,verbose_name='Creado')
    update_at=models.DateTimeField(auto_now=True,verbose_name='Editado')

    class Meta:
        verbose_name='Horario'
        verbose_name_plural='Horarios'
        
    def __str__(self):
        return str(self.nombre)

class Asistencia(models.Model):
    Horario=models.ManyToManyField(Horarios, verbose_name="Horarios", blank=True)
    Lista=models.ManyToManyField(Listas, verbose_name="Listas", blank=True)
    asiste=models.BooleanField(verbose_name='Asistencia',blank='true')
    create_at=models.DateTimeField(auto_now_add=True,verbose_name='Creado')
    update_at=models.DateTimeField(auto_now=True,verbose_name='Editado')

    class Meta:
        verbose_name='Asistencia'
        verbose_name_plural='Asistencias'
        
    def __str__(self):
        return str(self.nombre)
