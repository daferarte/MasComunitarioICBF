from django.contrib import admin
from .models import Personas, TipoDocumento


# Register your models here.
class PersonasAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'create_at', 'update_at')
    search_fields = ('tipoDocumento', 'cedula', 'user__username', 'fNacimiento')
    list_filter = ('public',)
    list_display = ('cedula', 'public', 'create_at', 'user')
    ordering = ('-create_at',)

    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user_id = request.user.id
        obj.save()


class TipoDocumentoAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at', 'update_at')
    search_fields = ('nombre', 'Personas__cedula', 'fNacimiento')
    list_display = ('nombre', 'create_at', 'update_at')
    ordering = ('-create_at',)


admin.site.register(Personas, PersonasAdmin)
admin.site.register(TipoDocumento, TipoDocumentoAdmin)
