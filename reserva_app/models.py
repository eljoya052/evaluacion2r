from django.db import models

# Create your models here.

class reserva(models.Model):
    nombre=models.CharField(max_length=50)
    telefono=models.CharField(max_length=9)
    fecha_reserva=models.DateField()
    hora=models.TimeField()
    cantidad_persona=models.IntegerField(max_length=15)
    estado=models.CharField(max_length=50)
    observacion=models.CharField(max_length=50)
