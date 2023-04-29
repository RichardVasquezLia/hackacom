from plantitas.models import Planta
from plantitas.serializers import PlantitasSerializer
from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import render
from PIL import Image
import numpy as np
from tensorflow.keras.utils import img_to_array
import tensorflow as tf
from tensorflow.keras.utils import load_img
from keras.models import load_model
from rest_framework import status


# Create your views here.
class PlantasCreateView(generics.ListCreateAPIView):
    queryset = Planta.objects.all()
    serializer_class = PlantitasSerializer

    def post(self, request, *args, **kwargs):
        print("esta dentro del post")
        try:
            longitud, altura = 150, 150                
            modelo = 'C:/Users/Shick/Documents/hackaton/hackacom/back/modelo.h5'
            pesos_modelo = 'C:/Users/Shick/Documents/hackaton/hackacom/back/pesos.h5'
            cnn = load_model(modelo)
            cnn.load_weights(pesos_modelo)
            batch_size = 32
            img_height = 150
            img_width = 150

            train_ds = tf.keras.utils.image_dataset_from_directory(
            # 'C:/Users/arnol/Downloads/apple/train',        
            'C:/Users/Shick/Documents/hackaton/hackacom/back/train',         
            validation_split=0.2,
            subset="training",
            seed=123,
            image_size=(img_height, img_width),
            batch_size=batch_size)
 

            class_names = train_ds.class_names
            longitud, altura = 150, 150
            # dir_path = "C:/Users/arnol/Downloads/apple/test/Apple___healthy/hoja.jpg"
            dir_path = self.image
            x = load_img(dir_path, target_size=(longitud, altura))
            x = img_to_array(x)
            x = np.expand_dims(x, axis=0)
            predictions = cnn.predict(x)
            print(predictions)
            score = tf.nn.softmax(predictions[0])
            print(score)
            print(
                "This image most likely belongs to {} with a {:.2f} percent confidence."
                .format(class_names[np.argmax(score)], 100 * np.max(score))
            )
        except Exception as e:
            print('fallo la prediccion', e)
        return Response('prueba', status= status.HTTP_200_OK)


class PlantasUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Planta.objects.all()
    serializer_class = PlantitasSerializer




