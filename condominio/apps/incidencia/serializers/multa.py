from rest_framework import serializers
from ..models import Multa,TipoMulta
from ...usuario.models import User

class TipoMultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoMulta
        fields = ['id','nombre','descripcion']
        
class MultaSerializer(serializers.ModelSerializer):
    usuario = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    tipo = serializers.PrimaryKeyRelatedField(queryset=TipoMulta.objects.all())
    class Meta:
        model = Multa
        fields = ['id','descripcion','estado','tipo','usuario']

