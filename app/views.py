from django.shortcuts import render
from django.http import JsonResponse, Http404
from app.models import *
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

def index(request):
    return render(request, 'app/index.html')

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
       
class CustomLoginForm(AuthenticationForm):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    print(self.fields['username'].label)
    self.fields['username'].widget.attrs.update(
      {'class': 'w-full px-4 py-2 mt-2 border rounded-md focus:outline-none focus:ring-1 focus:ring-blue-600'}
    )
    self.fields['password'].widget.attrs.update(
      {'class': 'w-full px-4 py-2 mt-2 border rounded-md focus:outline-none focus:ring-1 focus:ring-blue-600'}
    )