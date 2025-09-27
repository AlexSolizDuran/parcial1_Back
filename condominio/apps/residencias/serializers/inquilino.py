from rest_framework import serializers
from ..models import Inquilino,Mascota,Contrato,Ocupante,Vivienda
from ...usuario.models import User

class InquilinoSerializer(serializers.ModelSerializer):
    usuario = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    contrato = serializers.PrimaryKeyRelatedField(queryset=Contrato.objects.all())
    class Meta:
        model = Inquilino
        fields = ['id','estado', 'usuario', 'contrato']
        
class MascotaSerializer(serializers.ModelSerializer):
    inquilino = serializers.PrimaryKeyRelatedField(queryset=Inquilino.objects.all())
    class Meta:
        model = Mascota
        fields = ['id','nombre', 'especie', 'raza', 'inquilino']
        
class OcupanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ocupante
        fields = ['id','persona_ci', 'estado', 'contrato']

class ContratoSerializer(serializers.ModelSerializer):
    vivienda = serializers.PrimaryKeyRelatedField(queryset=Vivienda.objects.all())
    class Meta:
        model = Contrato
        fields = ['id','descripcion', 'fecha_ingreso', 'fecha_salida', 
                  'porcentaje_expensa', 'tipo_renta', 'vivienda']