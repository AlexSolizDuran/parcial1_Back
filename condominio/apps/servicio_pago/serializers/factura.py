from rest_framework import serializers
from ..models import Factura,DetalleFactura

class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = ['id','nro_factura', 'descripcion', 'fecha_emision', 'monto_total', 'estado', 'usuario']


class DetalleFacturaSerializer(serializers.ModelSerializer):
    factura = serializers.PrimaryKeyRelatedField(queryset=Factura.objects.all())

    class Meta:
        model = DetalleFactura
        fields = ['id','descripcion', 'monto', 'factura']