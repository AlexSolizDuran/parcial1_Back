from rest_framework import serializers
from ..models import ExpensaVivienda
from ...residencias.models.vivienda import Vivienda

class ExpensaViviendaSerializer(serializers.ModelSerializer):
    vivienda = serializers.PrimaryKeyRelatedField(queryset=Vivienda.objects.all())

    class Meta:
        model = ExpensaVivienda
        fields = ['id','fecha_emision', 'fecha_vencimiento', 'monto', 'estado', 'vivienda']
