from django.db import models

class Planta(models.Model):
    nombre = models.CharField(max_length=30)
    tipo_planta = models.CharField(max_length=30)
    enfermedad = models.BooleanField()
    descripcion_enfermedad = models.CharField(max_length=500)
    imagen_dir = models.CharField(max_length=250)
