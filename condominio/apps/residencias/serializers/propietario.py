from rest_framework import serializers
from ..models import Propietario, Parqueo, NumeroParqueo
from ...usuario.models import User
from ...usuario.serializers import UserSerializer


class PropietarioSerializer(serializers.ModelSerializer):
    usuario = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),write_only=True)
    usuario_detail = UserSerializer(source='usuario',read_only=True)
    
    class Meta:
        model = Propietario
        fields = ['id','usuario','usuario_detail', 'estado', 'fecha_compra', 'QRpago']
        
class ParqueoSerializer(serializers.ModelSerializer):
    propietario = serializers.PrimaryKeyRelatedField(queryset=Propietario.objects.all())
    class Meta:
        model = Parqueo
        fields = ['id','descripcion', 'propietario']

class NumeroParqueoSerializer(serializers.ModelSerializer):
    parqueo = serializers.PrimaryKeyRelatedField(queryset=Parqueo.objects.all())
    class Meta:
        model = NumeroParqueo
        fields = ['id','inquilino_id', 'parqueo', 'numero']