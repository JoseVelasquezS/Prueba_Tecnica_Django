from typing import Any
from django.db.models import fields
from django.forms.forms import DeclarativeFieldsMetaclass
from django.shortcuts import render
from django.http import request
from django.http import HttpResponse
from Modulos.perfil_api.forms import *
from Modulos.perfil_api.models import *
from django.core import serializers
import json


def crear(request):
    #   todoslosprodcutos: productos().objects.all()
    context = {
        'productos': productos.objects.all(),
        'form' : formulario()
    }
    return render (request, 'formulario.html', context)
def front(request):
    #   todoslosprodcutos: productos().objects.all()
    context = {
        'productos': productos.objects.all(),
        'form' : formulario()
    }
    return render (request, 'Prueba.html', context)    

def crearPost(request):
    if request.method == 'POST':
        
        producto_texto = request.POST.get('producto')
        descripcion_texto = request.POST.get('descripcion')
        precio_texto = request.POST.get('precio')
        data = {}
        crear_publicacion, created = productos.objects.get_or_create(
            nombre= producto_texto,
            descripcion = descripcion_texto,
            precio = precio_texto
        )
        
        data['resultado'] = "envio de datos exitoso"
        data['codigo'] = crear_publicacion.pk
        data['nombre'] = crear_publicacion.nombre
        data['descripcion'] = crear_publicacion.descripcion
        data['precio'] = crear_publicacion.precio

        return HttpResponse (
            json.dumps(data),
            content_type='aplication/json'  
            
        )
    else: 
        return HttpResponse ( 
            "algo anda mal" 
            
        )
def crearDetalle(request):
    if request.method == 'POST':
        #productos object (1)
        
        id_Producto = request.POST.get('idProducto')
        cantidad_= request.POST.get('cantidad')
        precio_= request.POST.get('precio')
        data = {}        
        busqueda= serializers.serialize('json', productos.objects.filter(pk=id_Producto))      
        if (request.POST.get('precio')):
            a = productos.objects.get(id=id_Producto)     
          

            crear_detalle, created = detalles_productos.objects.get_or_create(
            idProducto = a,
            cantidad = cantidad_,
            valorTotal = float(precio_) * float(cantidad_),
            valorIva = (float(precio_) * float(cantidad_))* 0.19
        )
            return HttpResponse(
                "salio")
        else: 
            return HttpResponse(
                busqueda)

    else: 
        return HttpResponse ( 
            "algo anda mal" 
            
        )

def verDetalle(request):
    if request.method == 'POST':
        id_Detalle = request.POST.get('detalle')
        daticos= serializers.serialize('json', detalles_productos.objects.filter(pk=id_Detalle))
        return HttpResponse( daticos
        )
    else: 
        return HttpResponse ( 
            "algo anda mal"
        )
def llamar(request):
    if request.method == 'GET':
        datos ={}
        datos = productos.objects.all()
        daticos= serializers.serialize('json', productos.objects.all())
        return HttpResponse( daticos
            
        )
    else: 
        return HttpResponse ( 
            "algo anda mal"
        )
def llamarDetalle(request):
    if request.method == 'GET':
        datos ={}
        datos = productos.objects.all()
        daticos= serializers.serialize('json', detalles_productos.objects.all())
        return HttpResponse( daticos
            
        )
    else: 
        return HttpResponse ( 
            "algo anda mal"
        )      
def editar(request):
    if request.method == 'PUT':
        datos ={}
        return HttpResponse( "Hecho"
            
        )
    else: 
        return HttpResponse ( 
            "algo anda mal")