from django.contrib import admin
from .forms import NotaModelForm
from .models import Nota, Area


class AdminNota (admin.ModelAdmin):
    list_display = ['id', 'area', 'estado',
                    'fecha_recibido', 'fecha_confirmado']
    form = NotaModelForm
    search_fields = ['estado', 'area']
    # exclude = ['estado', 'fecha_confirmado']
    # --> esto dice q no puedo usar cuando uso un ModelForm

    class Meta:
        model = Nota


admin.site.register(Nota, AdminNota)
admin.site.register(Area)
