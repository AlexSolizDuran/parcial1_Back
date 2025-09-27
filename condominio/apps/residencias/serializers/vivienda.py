from rest_framework import serializers
from ...admin_condominio.models import Condominio
from ..models import Vivienda,HistorialDueño,Propietario

class ViviendaSerializer(serializers.ModelSerializer):
    condominio = serializers.PrimaryKeyRelatedField(queryset=Condominio.objects.all())
    propietario = serializers.PrimaryKeyRelatedField(queryset=Propietario.objects.all())
    class Meta:
        model = Vivienda
        fields = ['condominio', 'propietario', 'nro_vivienda', 
                  'precio_alquiler', 'precio_anticretico', 'superfice', 'estado']
        

class HistorialDueñoSerializer(serializers.ModelSerializer):
    vivienda = serializers.PrimaryKeyRelatedField(queryset=Vivienda.objects.all())
    class Meta:
        model = HistorialDueño
        fields = ['estado', 'fecha_inicio', 'fecha_fin', 'propietario_id', 'vivienda']
        
