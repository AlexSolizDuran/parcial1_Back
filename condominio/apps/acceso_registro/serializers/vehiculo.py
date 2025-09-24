from rest_framework import serializers
from ..models import Vehiculo
from ...usuario.models import Persona


class VehiculoSerializer(serializers.ModelSerializer):
    persona = serializers.PrimaryKeyRelatedField(queryset=Persona.objects.all())
    class Meta:
        model = Vehiculo
        fields = ['color','modelo','placa','persona']
        