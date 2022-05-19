from ast import For
from django.shortcuts import render
from django.http import JsonResponse, Http404
from app.models import *
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.forms.models import model_to_dict
from django.conf import settings

def index(request):
    return render(request, 'app/index.html')

@login_required
def todosRegistros(request):
    registros = Registro.objects.all()
    contexto = {
        "registros": list(registros)
    }
    
    return render(request, 'app/registros.html', contexto)

def prueba(request):
  return render(request, 'app/example.html')

@login_required  
def showRegistros(request, id_sensor):
    id_sensores = []
    sensores = Sensor.objects.filter(usuario=request.user.id)
    for sensor in sensores:
      id_sensores.append(sensor.id)
    
    sensor = Sensor.objects.get(id=id_sensor)
    sensor_dict = model_to_dict(sensor)
    registros = Registro.objects.filter(sensor_id = id_sensor).values()
    contexto = {
      'sensor':sensor_dict,
      'sensores': list(id_sensores),
      'registros': list(registros),
      'media_url': settings.MEDIA_URL
    }
    return render(request, 'app/registros.html', contexto)

@login_required
def panelControl(request):
    username = request.user.username
    sensores = Sensor.objects.filter(usuario = request.user)
    dispositivos = Dispositivo.objects.filter(usuario = request.user)
    contexto = {
        "username": username,
        "sensores": list(sensores),
        "dispositivos": list(dispositivos)
    }
    return render(request, 'app/dashboard.html', contexto)     

@login_required
def galeria(request):
  registros_sensor = []
  registros_imagen = []
  sensores = Sensor.objects.filter(usuario = request.user)
  
  for sensori in sensores:
    registros_sensor = Registro.objects.filter(sensor = sensori)
    for registro in registros_sensor:
      if(not registro.imagen is None):
        registros_imagen.append({
          'fecha':str(registro.fecha_hora),
          'nombre_sensor':registro.sensor.nombre,
          'imagen':registro.imagen
        })
  
  contexto = {
      'registros_imagen':registros_imagen,
      'media_root': settings.MEDIA_ROOT,
      'media_url': settings.MEDIA_URL
  }
  return render(request, 'app/galeria.html', contexto)
  