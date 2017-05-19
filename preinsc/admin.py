from .models import Ficha, Tutor
from django.contrib import admin


class AdminTutor (admin.ModelAdmin):
    list_display = ['dni', 'apellido', 'nombre',
                    'telefono', 'email', 'fecha_alta']

    search_fields = ['dni', 'apellido', 'nombre']

    class Meta:
        model = Tutor


class AdminFicha (admin.ModelAdmin):
    fieldsets = [('Datos del niño', {'fields': ['dni', 'apellido', 'nombre',
                                                'fecha_nacimiento', 'domicilio', 'vive_con']
                                     }
                  ),
                 ('Datos de los padres o tutores', {'fields': ['mama', 'papa']
                                                    }
                  ),

                 ('Informacion general', {'fields': ['descripcion']}),
                 ]

    list_display = ['dni', 'apellido', 'nombre',
                    'fecha_nacimiento', 'estado', 'fecha_alta']

    search_fields = ['dni', 'apellido', 'nombre']

    class Meta:
        model = Ficha


admin.site.register(Ficha, AdminFicha)
admin.site.register(Tutor, AdminTutor)
