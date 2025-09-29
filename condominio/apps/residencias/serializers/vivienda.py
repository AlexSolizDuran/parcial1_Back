from rest_framework import serializers
from ...admin_condominio.models import Admin,AdminCondominio
from ..models import Vivienda,HistorialDueño,Propietario,PropietarioVivienda

class ViviendaSerializer(serializers.ModelSerializer):
    condominio = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Vivienda
        fields = ['id','condominio', 'nro_vivienda',
                  'precio_alquiler', 'precio_anticretico', 'superficie', 'estado','foto']
    
    def create(self, validated_data):
        user = self.context['request'].user
        admin = Admin.objects.filter(usuario=user).first()
        condomininio = AdminCondominio.objects.filter(admin=admin, activo=True).first().condominio
        validated_data['condominio'] = condomininio
        return super().create(validated_data)
        

class HistorialDueñoSerializer(serializers.ModelSerializer):
    vivienda = serializers.PrimaryKeyRelatedField(queryset=Vivienda.objects.all())
    class Meta:
        model = HistorialDueño
        fields = ['id','estado', 'fecha_inicio', 'fecha_fin', 'propietario_id', 'vivienda']
        
class PropietarioViviendaSerializer(serializers.ModelSerializer):
    propietario = serializers.PrimaryKeyRelatedField(queryset=Propietario.objects.all())
    vivienda = ViviendaSerializer(read_only=True)
    class Meta:
        model = PropietarioVivienda
        fields = ['id','estado', 'propietario', 'vivienda']
        
    