from django.contrib import admin
from .models import *

# Register your models here.
class GruposAdmin(admin.ModelAdmin):
    readonly_fields=('create_at','update_at')
    search_fields = ('nombre','Personas__cedula','fNacimiento')
    #list_filter=('public',)
    list_display = ('nombre','create_at','update_at')
    ordering=('-create_at',)

admin.site.register(Grupos, GruposAdmin)