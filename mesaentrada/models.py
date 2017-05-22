from django.db import models
from preinsc.models import Ficha


class Area(models.Model):
    nombre = models.CharField(max_length=20)
    fecha_alta = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.nombre


class PesonalColegio(models.Model):
    nombre = models.CharField(max_length=20)
    fecha_alta = models.DateTimeField(auto_now_add=True, auto_now=False)
    area = models.ForeignKey(
        Area, null=False, blank=False,)

    def __str__(self):
        return self.nombre


class Nota(models.Model):
    # los string se guardan en la BD
    RECIBIDA = 'Recibida'
    CONFIRMADA = 'Confirmada'
    RESPONDIDA = 'Respondida'
    DERIVADA = 'Derivada'

    ESTADOS_DE_NOTA = (
        (RECIBIDA, 'Recibida'),
        (CONFIRMADA, 'Confirmada'),
        (RESPONDIDA, 'Respondida'),
        (DERIVADA, 'Derivada'),
    )

    personal = models.ForeignKey(PesonalColegio, null=True, blank=True, default=0) 
    idficha = models.ForeignKey(Ficha)
    area = models.ForeignKey(
        Area, null=False, blank=False,
        default='Administracion')

    estado = models.CharField(
        max_length=10,
        choices=ESTADOS_DE_NOTA,
        default=RECIBIDA,
    )

    fecha_recibido = models.DateTimeField(auto_now_add=True, auto_now=False)
    fecha_confirmado = models.DateTimeField(null=True, blank=True)
    descripcion = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return str(self.id)
