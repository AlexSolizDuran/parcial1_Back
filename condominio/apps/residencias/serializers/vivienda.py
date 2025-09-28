from rest_framework import serializers
from ...admin_condominio.models import Condominio
from ..models import Vivienda,HistorialDueño,Propietario,PropietarioVivienda
from ..serializers import PropietarioSerializer


class ViviendaSerializer(serializers.ModelSerializer):
    condominio = serializers.PrimaryKeyRelatedField(queryset=Condominio.objects.all())
    class Meta:
        model = Vivienda
        fields = ['id','condominio', 'nro_vivienda',
                  'precio_alquiler', 'precio_anticretico', 'superfice', 'estado','foto']
        

class HistorialDueñoSerializer(serializers.ModelSerializer):
    vivienda = serializers.PrimaryKeyRelatedField(queryset=Vivienda.objects.all())
    class Meta:
        model = HistorialDueño
        fields = ['id','estado', 'fecha_inicio', 'fecha_fin', 'propietario_id', 'vivienda']
        
class PropietarioViviendaSerializer(serializers.ModelSerializer):
    propietario = serializers.PrimaryKeyRelatedField(queryset=Propietario.objects.all())
    vivienda = ViviendaSerializer(read_only=True)
    class Meta:
        model = PropietarioVivienda
        fields = ['id','estado', 'propietario', 'vivienda']
        
    