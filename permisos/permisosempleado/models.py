from django.db import models

# Create your models here.

class Empleado(models.Model):


    ENFERMEDAD = 'ENFERMEDAD'
    COMPENSACION = 'COMPENSACION'
    CALAMIDAD = 'CALAMIDAD'
    CERTIFICADO = 'CERTIFICADO'
    TIPO_AUSENSIA_CHOICES = (
        (ENFERMEDAD, 'ENFERMEDAD'),
        (COMPENSACION, 'COMPENSACION'),
        (CALAMIDAD, 'CALAMIDAD'),
        (CERTIFICADO, 'CERTIFICADO'),
    )
    tipoPermiso = models.CharField(
        max_length=15,
        choices=TIPO_AUSENSIA_CHOICES,
        default=ENFERMEDAD,
    )


    nombreCompleto = models.CharField(max_length = 30, blank = False, null = False)
    fechaDesde = models.DateField('fecha de desde')
    fechaHasta = models.DateField('fecha de hasta')
    numeroDias = models.IntegerField()


class Meta:
    verbose_name = 'empleado'
    verbose_name = 'empleados'
    verbose_name = ['nombreCompleto']

def __str__(self):
    return self.nombreCompleto
