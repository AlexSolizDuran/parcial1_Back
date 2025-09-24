from rest_framework import serializers
from ..models import Pago,TipoPago,Factura


class TipoPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPago
        fields = ['nombre', 'descripcion']

class PagoSerializer(serializers.ModelSerializer):
    tipo_pago = serializers.PrimaryKeyRelatedField(queryset=TipoPago.objects.all())
    factura = serializers.PrimaryKeyRelatedField(queryset=Factura.objects.all())

    class Meta:
        model = Pago
        fields = ['fecha_pago','monto','tipo_pago','factura']