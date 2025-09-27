from rest_framework import serializers
from ..models import Gasto,Condominio,Admin

class GastoSerializers(serializers.ModelSerializer):
    condominio = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Gasto
        fields = ['id','descripcion', 'monto','condominio']
        
    def create(self, validated_data):
        user = self.context['request'].user  # admin logueado
        admin = Admin.objects.get(usuario=user)  # obtener objeto Admin del usuario
        validated_data['condominio'] = admin.condominio  # asignar condominio automáticamente
        return super().create(validated_data)