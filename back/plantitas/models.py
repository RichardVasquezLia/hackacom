from django.db import models
from PIL import Image
import numpy as np
from tensorflow.keras.utils import img_to_array
import tensorflow as tf
from tensorflow.keras.utils import load_img
from keras.models import load_model

class Planta(models.Model):
    nombre = models.CharField(max_length=30)
    tipo_planta = models.CharField(max_length=30)
    enfermedad = models.BooleanField()
    descripcion_enfermedad = models.CharField(max_length=500)
    imagen_dir = models.CharField(max_length=250)

    def __str__(self):
        return self.name
    
    
