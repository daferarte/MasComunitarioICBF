from django.db import models
from grupos.models import Grupos
from django.contrib.auth.models import User

# Create your models here.
estados_curso=[
    (1,'Disponible'),
    (2,'No Disponible')
]

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
    #nombre=models.CharField(max_length=100, verbose_name='Numero clase')
    nombre=models.IntegerField(
        null=False,blank=False,
        choices=estados_curso
    )
    Fecha=models.DateTimeField(verbose_name='Fecha')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    create_at=models.DateTimeField(auto_now_add=True,verbose_name='Creado')
    update_at=models.DateTimeField(auto_now=True,verbose_name='Editado')

    class Meta:
        verbose_name='Horario'
        verbose_name_plural='Horarios'
        
    def __str__(self):
        return str(self.nombre)

class Asistencia(models.Model):
    Horario=models.ForeignKey(Horarios, verbose_name="Horarios", blank=True, on_delete=models.CASCADE, null=True)
    Lista=models.ForeignKey(Listas, verbose_name="Listas", blank=True, on_delete=models.CASCADE, null=True)
    asiste=models.BooleanField(verbose_name='Asistencia',blank=True, default=False)
    create_at=models.DateTimeField(auto_now_add=True,verbose_name='Creado')
    update_at=models.DateTimeField(auto_now=True,verbose_name='Editado')

    class Meta:
        verbose_name='Asistencia'
        verbose_name_plural='Asistencias'
        
    def __str__(self):
        return str(self.create_at)
