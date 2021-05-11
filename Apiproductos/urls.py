"""Apiproductos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Modulos.perfil_api.views import (crear,front, crearDetalle, crearPost,llamar,editar,verDetalle, llamarDetalle)


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', crear, name='crear'),
    path('crearPost/', crearPost, name='crearPost'),
    path('llamar/', llamar, name='llamar'),
    path('crearDetalle/', crearDetalle, name='crearDetalle'),
    path('llamarDetalle/', llamarDetalle, name='llamarDetalle'),
    path('verDetalle/', verDetalle, name='verDetalle'),

    

]
