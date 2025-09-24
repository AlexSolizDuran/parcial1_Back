from rest_framework import serializers
from ..models.visitante import TipoVisita, Visitante
from ...usuario.models import Persona


class VisitanteSerializer(serializers.ModelSerializer):
    persona = serializers.PrimaryKeyRelatedField(queryset=Persona.objects.all())
    tipo_visita = serializers.PrimaryKeyRelatedField(queryset=TipoVisita.objects.all())
    class Meta:
        model = Visitante
        fields = ['persona','tipo_visita','fecha_visita','motivo','estado']

class TipoVisitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoVisita
        fields = ['nombre']
