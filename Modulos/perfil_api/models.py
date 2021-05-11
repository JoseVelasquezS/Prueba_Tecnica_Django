from django.db import models
from djmoney.models.fields import MoneyField

# Create your models here.

class productos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    

    precio = models.FloatField(max_length=20)
    #precio = models.FloatField(max_length=20)
    descripcion = models.TextField()
    

class detalles_productos(models.Model):
    id = models.AutoField(primary_key=True)
    idProducto = models.ForeignKey(productos, null=False, blank=False, on_delete=models.CASCADE)
    cantidad = models.FloatField(max_length=20)
    valorTotal = models.FloatField(max_length=20)
    valorIva = models.FloatField(max_length=20)



