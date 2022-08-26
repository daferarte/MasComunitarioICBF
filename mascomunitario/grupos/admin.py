from django.contrib import admin
from .models import Grupos


# Register your models here.
class GruposAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at', 'update_at')
    search_fields = ('nombre', 'Personas__cedula', 'fNacimiento')
    list_display = ('nombre', 'create_at', 'update_at')
    ordering = ('-create_at',)


admin.site.register(Grupos, GruposAdmin)
