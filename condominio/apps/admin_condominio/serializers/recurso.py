from rest_framework  import serializers
from ..models import Recurso,TipoRecurso,Condominio,Admin,AdminCondominio


class TipoRecursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoRecurso
        fields = ['id','nombre', 'descripcion']
        
class RecursoSerializer(serializers.ModelSerializer):
    condominio = serializers.PrimaryKeyRelatedField( read_only=True)
    tipo_recurso = serializers.PrimaryKeyRelatedField(queryset=TipoRecurso.objects.all())
    class Meta:
        model = Recurso
        fields = ['id','nombre', 'descripcion', 'estado', 'condominio', 'tipo_recurso']
        
    def create(self, validated_data):
        user = self.context['request'].user  # admin logueado
        admin = Admin.objects.get(usuario=user) 
        admin_condominio = AdminCondominio.objects.filter(admin=admin, activo=True).first()
        validated_data['condominio'] = admin_condominio.condominio  # asignar condominio automáticamente
        return super().create(validated_data)