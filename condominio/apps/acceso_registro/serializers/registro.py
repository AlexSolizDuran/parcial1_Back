from rest_framework import serializers
from ..models import Registro,Seguridad
from ...admin_condominio.models import AdminCondominio,Admin
from ...usuario.models import User


class SeguridadSeriliazer(serializers.ModelSerializer):
    usuario = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    condominio = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Seguridad
        fields = ['usuario','condominio','turno','estado']
        
    def create(self, validated_data):
        user = self.context['request'].user
        admin = Admin.objects.filter(usuario=user).first()
        condomininio = AdminCondominio.objects.filter(admin=admin, activo=True).first().condominio
        validated_data['condominio'] = condomininio
        return super().create(validated_data)

        

class RegistroSerializer(serializers.ModelSerializer):
    condominio = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Registro
        fields = ['ci_persona_entrante',
                  'ci_persona_saliente',
                  'fecha_ingreso',
                  'fecha_salida',
                  'condominio',
                  'vehiculo_id',
                  'seguridad_id',
                  'motivo']
    def create(self, validated_data):
        user = self.context['request'].user
        admin = Admin.objects.filter(usuario=user).first()
        admin_condominio = AdminCondominio.objects.filter(admin=admin, activo=True).first()
        if admin_condominio is None:
            seguridad = Seguridad.objects.filter(usuario=user).first()  # obtener objeto Seguridad del usuario)
        else:
            validated_data['condominio'] = admin_condominio.condominio # asignar condominio automáticamente

        validated_data['condominio'] = seguridad.condominio  # asignar condominio automáticamente
        return super().create(validated_data)