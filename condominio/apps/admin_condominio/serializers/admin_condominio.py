from rest_framework import serializers
from ..models import AdminCondominio,Admin,Condominio
from ...usuario.serializers import UserSerializer


class AdminSerializer(serializers.ModelSerializer):
    usuario = serializers.PrimaryKeyRelatedField(queryset=UserSerializer.Meta.model.objects.all())
    class Meta:
        model = Admin
        fields = ['usuario','activo']

class CondominioSerializer(serializers.ModelSerializer):
    admin = AdminSerializer(many=True,read_only=True)
    class Meta:
        model = Condominio
        fields = ['nombre', 'direccion', 'telefono', 'QR', 'cantidad_viviendas', 'admin']

class AdminCondominioSerializer(serializers.ModelSerializer):
    admin = serializers.PrimaryKeyRelatedField(queryset=Admin.objects.all())
    condominio = serializers.PrimaryKeyRelatedField(queryset=Condominio.objects.all())
    class Meta:
        model = AdminCondominio
        fields = ['admin', 'condominio','activo']