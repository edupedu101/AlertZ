from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Sensor(models.Model):
    nombre = models.CharField(max_length=50)
    modelo = models.CharField(max_length=100)
    desc = models.TextField(default=None, blank=True, null=True)
    tipo_sensor = models.CharField(max_length=20)    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
    
class Registro(models.Model):
    fecha_hora = models.DateTimeField()
    sensor = models.ForeignKey(Sensor, on_delete=models.DO_NOTHING)
    def __str__(self):
        return str(self.fecha_hora)
    
class Imagen(models.Model):
    nombre = models.CharField(max_length=50, default=True)
    registro = models.OneToOneField(Registro ,on_delete=models.DO_NOTHING, null=False, primary_key=True) 
    imagen = models.ImageField(blank=False, default=None)