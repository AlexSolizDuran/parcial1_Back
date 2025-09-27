from rest_framework import serializers
from ..models import Expensa,TipoExpensa
from ...admin_condominio.models.admin_condominio import Condominio


class TipoExpensaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoExpensa
        fields = ['id','nombre', 'descripcion']
        
class ExpensaSerializer(serializers.ModelSerializer):
    condominio = serializers.PrimaryKeyRelatedField(queryset=Condominio.objects.all())
    tipo_expensa = serializers.PrimaryKeyRelatedField(queryset=TipoExpensa.objects.all())

    class Meta:
        model = Expensa
        fields = ['id','estado', 'fecha_vencimiento', 'monto', 'tipo_expensa','condominio']
        
