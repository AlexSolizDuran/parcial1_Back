from rest_framework import serializers
from ...admin_condominio.models import Condominio
from ..models import Vivienda,HistorialDueño,Propietario,PropietarioVivivienda

class ViviendaSerializer(serializers.ModelSerializer):
    condominio = serializers.PrimaryKeyRelatedField(queryset=Condominio.objects.all())
    propietario = serializers.PrimaryKeyRelatedField(queryset=Propietario.objects.all())
    class Meta:
        model = Vivienda
        fields = ['id','condominio', 'propietario', 'nro_vivienda',
                  'precio_alquiler', 'precio_anticretico', 'superfice', 'estado','foto']
        

class HistorialDueñoSerializer(serializers.ModelSerializer):
    vivienda = serializers.PrimaryKeyRelatedField(queryset=Vivienda.objects.all())
    class Meta:
        model = HistorialDueño
        fields = ['id','estado', 'fecha_inicio', 'fecha_fin', 'propietario_id', 'vivienda']
        
class PropietarioViviendaSerializer(serializers.ModelSerializer):
    propietario = serializers.PrimaryKeyRelatedField(queryset=Propietario.objects.all())
    vivienda = serializers.PrimaryKeyRelatedField(queryset=Vivienda.objects.all())
    class Meta:
        model = PropietarioVivivienda
        fields = ['id','estado', 'propietario', 'vivienda']