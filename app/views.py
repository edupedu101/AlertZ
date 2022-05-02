from django.shortcuts import render
from django.http import JsonResponse, Http404
from app.models import *
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required

def todosRegistros(request):
    registros = Registro.objects.all()
    contexto = {
        "registros": list(registros)
    }
    
    return render(request, 'app/registros.html', contexto)
    
def registros(request):
    sensores = Sensor.objects.filter(usuario =request.user)
    registros = Registro.objects.filter(sensor = sensores).values
    contexto = {
        "registros": list(registros)
    }
    
    return render(request, 'app/registros.html', contexto)
    
    
