from rest_framework import serializers
from ..models import Multa,TipoMulta
from ...usuario.models import User
from ...usuario.serializers import UserSerializer

class TipoMultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoMulta
        fields = ['id','nombre','descripcion']
        
class MultaSerializer(serializers.ModelSerializer):
    usuario = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),required=False,write_only=True)
    tipo = serializers.PrimaryKeyRelatedField(queryset=TipoMulta.objects.all())
    usuario_detail = UserSerializer(read_only=True)
    class Meta:
        model = Multa
        fields = ['id','descripcion','monto','estado','tipo','usuario','usuario_detail']
        
    def create (self,validated_data):
        request = self.context.get("request")  # El request completo
        user = request.user
        validated_data['usuario'] = user
        return super().create(validated_data)