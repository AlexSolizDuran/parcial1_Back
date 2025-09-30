from rest_framework import serializers
from ..models import Expensa,TipoExpensa
from ...admin_condominio.models import Admin,AdminCondominio
from ...admin_condominio.models.admin_condominio import Condominio


class TipoExpensaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoExpensa
        fields = ['id','nombre', 'descripcion']
        
class ExpensaSerializer(serializers.ModelSerializer):
    condominio = serializers.PrimaryKeyRelatedField(queryset=Condominio.objects.all(),write_only=True,required=False)
    tipo_expensa = serializers.PrimaryKeyRelatedField(queryset=TipoExpensa.objects.all(),write_only=True)
    tipo_expensa_detail  = serializers.SerializerMethodField()
    class Meta:
        model = Expensa
        fields = ['id','estado', 'fecha_vencimiento', 'monto', 'tipo_expensa','tipo_expensa_detail','condominio']    
    def get_tipo_expensa_detail(self, obj):
        if obj.tipo_expensa:
            return TipoExpensaSerializer(obj.tipo_expensa).data
        return None
    def create(self, validated_data):
        user = self.context['request'].user  # admin logueado
        admin = Admin.objects.get(usuario=user) 
        admin_condominio = AdminCondominio.objects.filter(admin=admin, activo=True).first()
        validated_data['condominio'] = admin_condominio.condominio
        return super().create(validated_data)
        
