from django.db import models


class Tutor(models.Model):
    dni = models.CharField(max_length=8, primary_key=True)
    apellido = models.CharField(max_length=20)
    nombre = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    domicilio = models.CharField(max_length=30)
    email = models.EmailField()
    fecha_alta = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.dni


class Ficha(models.Model):
    GANADOR = 'G'
    PREINSCRIPTO = 'P'
    RECHAZADO = 'R'
    CONFIRMADO = 'C'

    ESTADOS_DE_FICHA = (
        (GANADOR, 'Ganador'),
        (PREINSCRIPTO, 'Preinscripto'),
        (RECHAZADO, 'Rechazado'),
        (CONFIRMADO, 'Confirmado')
    )

    dni = models.CharField(max_length=8)
    apellido = models.CharField(max_length=20)
    nombre = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(null=False, blank=False)
    mama = models.ForeignKey(Tutor, related_name='mama')
    papa = models.ForeignKey(Tutor, related_name='papa')
    domicilio = models.CharField(max_length=20)
    vive_con = models.CharField(max_length=20)
    estado = models.CharField(
        max_length=10,
        choices=ESTADOS_DE_FICHA,
        default=PREINSCRIPTO,

    )

    fecha_alta = models.DateTimeField(auto_now_add=True, auto_now=False)
    descripcion = models.TextField(null=False, blank=False)

    def __str__(self):
        return str(self.dni)
