from django.shortcuts import render
from django.http import JsonResponse, Http404
from app.models import *
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

def index(request):
    return render(request, 'app/index.html')

@login_required
def todosRegistros(request):
    registros = Registro.objects.all()
    contexto = {
        "registros": list(registros)
    }
    
    return render(request, 'app/registros.html', contexto)
  
@login_required  
def registros(request):
    sensores = Sensor.objects.filter(usuario =request.user)
    registros = Registro.objects.filter(sensor = sensores).values
    contexto = {
        "registros": list(registros)
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
def showRegistros(request, id_sensor):
  registros = Registro.objects.filter(sensor = id_sensor)
  return render(request, "app/registros.html")