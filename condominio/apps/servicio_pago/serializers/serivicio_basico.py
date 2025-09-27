from rest_framework import serializers
from ..models import ServicioBasico
from ...residencias.models.vivienda import Vivienda



class ServicioBasicoSerializer(serializers.ModelSerializer):
    vivienda = serializers.PrimaryKeyRelatedField(queryset=Vivienda.objects.all())

    class Meta:
        model = ServicioBasico
        fields = ['id','nombre_empresa', 'numero_Factura', 'descripcion','image', 'costo', 
                  'fecha_fin', 'fecha_inicio', 'vivienda',]
