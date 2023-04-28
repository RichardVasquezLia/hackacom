from django.contrib import admin
from django.urls import path
from plantitas.views import PlantasCreateView, PlantasUpdateDelete

urlpatterns = [
    path("api/categorias/", PlantasCreateView.as_view()),
    path("api/categorias/<pk>/", PlantasUpdateDelete.as_view()),
]