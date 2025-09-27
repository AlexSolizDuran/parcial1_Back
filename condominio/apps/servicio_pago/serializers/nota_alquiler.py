from rest_framework import serializers
from ..models   import NotaAlquiler
from ...residencias.models.inquilino import Inquilino


class NotaAlquilerSerializer(serializers.ModelSerializer):
    inquilino = serializers.PrimaryKeyRelatedField(queryset=Inquilino.objects.all())
    class Meta:
        model = NotaAlquiler
        fields = ['id','fecha_emision', 'fecha_pago', 'monto_alquiler', 'monto_otros', 'estado', 'inquilino']    