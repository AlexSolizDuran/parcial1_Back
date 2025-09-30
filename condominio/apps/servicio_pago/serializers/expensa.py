from rest_framework import serializers
from ..models import Expensa,TipoExpensa
from ...admin_condominio.models import Admin,AdminCondominio
from ...admin_condominio.models.admin_condominio import Condominio


class TipoExpensaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoExpensa
        fields = ['id','nombre', 'descripcion']
        
class ExpensaSerializer(serializers.ModelSerializer):
    condominio = serializers.PrimaryKeyRelatedField(queryset=Condominio.objects.all(),write_only=True)
    tipo_expensa = serializers.PrimaryKeyRelatedField(queryset=TipoExpensa.objects.all(),write_only=True)
    tipo_expensa_detail  = TipoExpensaSerializer(read_only=True)
    class Meta:
        model = Expensa
        fields = ['id','estado', 'fecha_vencimiento', 'monto', 'tipo_expensa','tipo_expensa_detail','condominio']    
    def create(self, validated_data):
        user = self.context['request'].user
        admin = Admin.objects.filter(usuario=user).first()
        condomininio = AdminCondominio.objects.filter(admin=admin, activo=True).first().condominio
        validated_data['condominio'] = condomininio
        return super().create(validated_data)
        
