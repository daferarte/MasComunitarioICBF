from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TipoDocumento(models.Model):
    
    nombre=models.CharField(max_length=150, verbose_name='Nombre')
    descripcion=models.CharField(max_length=150, verbose_name='Descripción')
    create_at=models.DateTimeField(auto_now_add=True,verbose_name='Creado')
    update_at=models.DateTimeField(auto_now=True,verbose_name='Editado')   

    class Meta:
        verbose_name='Tipo de documento'
        verbose_name_plural='Tipos de documentos'
        
    def __str__(self):
        return str(self.nombre)
class Personas(models.Model):
    
    tipoDocumento = models.ManyToManyField(TipoDocumento, verbose_name="Tipo de documento", blank=True)
    cedula=models.CharField(max_length=150, verbose_name='Cedula')
    user=models.OneToOneField(User, editable=False, verbose_name="Usuario", on_delete=models.CASCADE) #clave relacional del modelo de usuarios de django
    image=models.ImageField(default='null', verbose_name="Imagen", upload_to="users")
    public=models.BooleanField(verbose_name="¿Publicado?")
    fNacimiento = models.DateField(null=True, blank=True, verbose_name="Fecha de cumpleaños" )
    create_at=models.DateTimeField(auto_now_add=True,verbose_name='Creado')
    update_at=models.DateTimeField(auto_now=True,verbose_name='Editado')    

    class Meta:
        verbose_name='Persona'
        verbose_name_plural='Personas'

    def __str__(self):
        return str(self.cedula)