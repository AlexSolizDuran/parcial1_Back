from rest_framework  import serializers
from ..models import Recurso,TipoRecurso,Condominio,Admin


class TipoRecursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoRecurso
        fields = ['nombre', 'descripcion']
        
class RecursoSerializer(serializers.ModelSerializer):
    condominio = serializers.PrimaryKeyRelatedField( read_only=True)
    tipo_recurso = serializers.PrimaryKeyRelatedField(queryset=TipoRecurso.objects.all())
    class Meta:
        model = Recurso
        fields = ['nombre', 'descripcion', 'estado', 'condominio', 'tipo_recurso']
        
    def create(self, validated_data):
        user = self.context['request'].user  # admin logueado
        admin = Admin.objects.get(usuario=user)  # obtener objeto Admin del usuario
        validated_data['condominio'] = admin.condominio  # asignar condominio automáticamente
        return super().create(validated_data)