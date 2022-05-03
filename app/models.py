from xmlrpc.client import Boolean
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Sensor(models.Model):
    class TipoSensor(models.TextChoices):
        PUERTA = 'Puerta', _('Puerta')
        CAMARA = 'Camara', _('Camara')
    nombre = models.CharField(max_length=50)
    modelo = models.CharField(max_length=100)
    desc = models.TextField(default=None, blank=True, null=True)
    tipo_sensor = models.CharField(max_length=11, choices=TipoSensor.choices, default=TipoSensor.PUERTA ,blank=False)    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
    
class Registro(models.Model):
    fecha_hora = models.DateTimeField()
    sensor = models.ForeignKey(Sensor, on_delete=models.DO_NOTHING)
    def __str__(self):
        return str(self.fecha_hora)
    
class Imagen(models.Model):
    nombre = models.CharField(max_length=50, default=True, null=False, blank=False)
    registro = models.OneToOneField(Registro ,on_delete=models.DO_NOTHING, null=False, primary_key=True) 
    imagen = models.ImageField(blank=False, default=None)

class Periferico(models.Model):
    class TipoPeriferico(models.TextChoices):
        VENTILADOR = 'Ventilador', _('Ventilador')
        LED = 'Led', _('Led')
    nombre = models.CharField(max_length=50, null=False, blank=False)
    modelo = models.CharField(max_length=50, null=False, blank=False)
    status = models.BooleanField(default=False, null=False, blank=False)
    tipo_periferico = models.CharField(max_length=11, choices=TipoPeriferico.choices, default=TipoPeriferico.LED ,blank=False)
    

    