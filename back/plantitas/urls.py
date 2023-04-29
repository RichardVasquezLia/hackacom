from django.contrib import admin
from django.urls import path
from plantitas.views import PlantasCreateView, PlantasUpdateDelete

urlpatterns = [
    path("api/plantitas/", PlantasCreateView.as_view()),
    path("api/plantitas/<pk>/", PlantasUpdateDelete.as_view()),
]