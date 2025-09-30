from rest_framework import serializers
from ..models import Reclamo,Foto
from ...usuario.models   import User

class ReclamoSerializer(serializers.ModelSerializer):
    usuario = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
    class Meta:
        model = Reclamo
        fields = ['id','descripcion','estado','fecha_resolucion','usuario']
    def create(self, validated_data):
        if 'usuario' not in validated_data:
            validated_data['usuario'] = self.context['request'].user
        return super().create(validated_data)
        
class FotoSerializer(serializers.ModelSerializer):
    reclamo = serializers.PrimaryKeyRelatedField(queryset=Reclamo.objects.all())
    class Meta:
        model = Foto
        fields = ['id','descripcion','image','reclamo']