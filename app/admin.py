from dataclasses import field
from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(Sensor)
admin.site.register(Registro)
admin.site.register(Imagen)
admin.site.register(Periferico)