from ast import For, expr_context
from django.http import JsonResponse
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.core.files.storage import default_storage
from app.models import *
from django.core.files import File
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.conf import settings
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes

import os, shutil, errno
import json
import datetime
from json import JSONEncoder


def ping(request):  
    if (request.method=='GET'):
        return JsonResponse({
            'status': 'OK',
            'ping': 'pong',
        })

# Enviar refcode y datetime por GET para añadir un registro

@api_view(['GET'])
@login_required
def getRegistros(request, id_sensor):
    registros = Registro.objects.filter(sensor = id_sensor)
    if (len(registros) == 0):
        raise Http404()
            
    return JsonResponse({
        'data':list(registros)
    })
    

@api_view(['GET'])
@login_required
def getSensores(request):
    sensores = Sensor.objects.filter(usuario = request.user.id)
    if (len(sensores) == 0):
        raise Http404()
    return JsonResponse({
        'data':list(sensores)
    })
    
@api_view(['GET'])
#@authentication_classes([BasicAuthentication])
#@permission_classes([IsAuthenticated])
def sensorRegistro(request):
    
    req_body = json.loads(request.body.decode('utf-8'))
    getRef=req_body['refcode']
    
    try:
        sensor= Sensor.objects.get(r_number=getRef)
    except:
        
        return Response({
            'status': 'ERROR',
            'message': 'Sensor desconocido'
        })  

    
    getDT=datetime.datetime.now()
    
    r = Registro(fecha_hora=getDT, sensor_id=sensor.id)
    
    try:
        r.save()
    except:
        return Response({
            'status': 'ERROR',
            'message': 'No se ha podido añadir el registro'
        })
    return Response({
        'status': 'OK',
        'message': 'Registro creado satisfactoriamente',
        'fecha': getDT,
    })

def sensorImagen(request):
    imagen = request.FILES["imagen"]
    req_body = json.loads(request.body.decode('utf-8'))
    getRef=req_body['refcode']
    try:
        sensor= Sensor.objects.get(r_number=getRef)
    except:
        
        return Response({
            'status': 'ERROR',
            'message': 'Sensor desconocido',
            'refcode': getRef
        })
    username=sensor.usuario.username
    static_dir = settings.STATICFILES_DIRS[0]
    try:
        new_dir_path = os.path.join(static_dir, "users", username)
    except:
        return Response({
            'status': 'ERROR',
            'message': 'no se puede crear la carpeta'
        })
    if not os.path.exists(new_dir_path):
        os.makedirs(new_dir_path)
    
    try:
        getDT=request.GET.get('imagen')
    except:
        return Response({
            'status': 'ERROR',
            'message': 'No se encuentra la imagen'
        })
    
    try:
        default_storage.save(new_dir_path, ContentFile(b'new content'))
    except:
        return Response({
            'status': 'ERROR',
            'message': 'No se ha podido guardar la imagen'
        })
           
