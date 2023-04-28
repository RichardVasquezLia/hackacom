from rest_framework.serializers import ModelSerializer
from plantitas.models import Planta

class PlantitasSerializer(ModelSerializer):
    class Meta:
        model = Planta
        fields = ('id','nombre','tipo_planta','enfermedad','descripcion_enfermedad','imagen_dir')
