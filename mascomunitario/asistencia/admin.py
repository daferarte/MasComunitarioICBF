from django.contrib import admin
from .models import *

# Register your models here.
class ListasAdmin(admin.ModelAdmin):
    readonly_fields=('create_at','update_at')
    search_fields = ('nombre','Apellido','cedula','fNacimiento')
    #list_filter=('public',)
    list_display = ('nombre','create_at','update_at')
    ordering=('-create_at',)

class HorariosAdmin(admin.ModelAdmin):
    readonly_fields=('create_at','update_at')
    search_fields = ('nombre','Fecha','Grupo__nombre')
    #list_filter=('public',)
    list_display = ('nombre','create_at','update_at')
    ordering=('-create_at',)

class AsistenciaAdmin(admin.ModelAdmin):
    readonly_fields=('create_at','update_at')
    search_fields = ('Horarios__nombre','Listas__cedula','create_at')
    #list_filter=('public',)
    list_display = ('create_at','update_at')
    ordering=('-create_at',)

admin.site.register(Listas, ListasAdmin)
admin.site.register(Horarios, HorariosAdmin)
admin.site.register(Asistencia, AsistenciaAdmin)