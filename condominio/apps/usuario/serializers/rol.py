from rest_framework import serializers
from ..models import Rol,RolUsuario
from .usuario import UserSerializer


class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ['nombre', 'descripcion']

class RolUsuarioSerializer(serializers.ModelSerializer):
    rol = RolSerializer()
    usuario = UserSerializer()
    class Meta:
        model = RolUsuario
        fields = ['usuario', 'rol']