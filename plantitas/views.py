from plantitas.models import Planta
from plantitas.serializers import PlantitasSerializer
from rest_framework import generics

from django.shortcuts import render
# Create your views here.
class PlantasCreateView(generics.ListCreateAPIView):
    queryset = Planta.objects.all()
    serializer_class = PlantitasSerializer

class PlantasUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Planta.objects.all()
    serializer_class = PlantitasSerializer