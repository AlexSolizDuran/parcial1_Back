from rest_framework import serializers
from ..models import Inquilino,Mascota,Contrato,Ocupante
from ...usuario.models import User

class InquilinoSerializer(serializers.ModelSerializer):
    usuario = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    contrato = serializers.PrimaryKeyRelatedField(queryset=Contrato.objects.all())
    class Meta:
        model = Inquilino
        fields = ['estado', 'usuario', 'contrato']
        
class MascotaSerializer(serializers.ModelSerializer):
    inquilino = serializers.PrimaryKeyRelatedField(queryset=Inquilino.objects.all())
    class Meta:
        model = Mascota
        fields = ['nombre', 'especie', 'raza', 'inquilino']
        
class OcupanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ocupante
        fields = ['persona_ci', 'estado', 'contrato']