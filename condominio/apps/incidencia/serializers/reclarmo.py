from rest_framework import serializers
from ..models import Reclamo,Foto
from ...usuario.models   import User

class ReclamoSerializer(serializers.ModelSerializer):
    usuario = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = Reclamo
        fields = ['id','descripcion','estado','usuario']
        
class FotoSerializer(serializers.ModelSerializer):
    reclamo = serializers.PrimaryKeyRelatedField(queryset=Reclamo.objects.all())
    class Meta:
        model = Foto
        fields = ['id','descripcion','image','reclamo']