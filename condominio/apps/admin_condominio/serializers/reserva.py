from rest_framework import serializers
from ..models import Reserva,Recurso
from ...usuario.models import User


class ReservaSerializer(serializers.ModelSerializer):
    usuario = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    recurso = serializers.PrimaryKeyRelatedField(queryset=Recurso.objects.all())
    class Meta:
        model = Reserva
        fields = ['id','descripcion', 'estado', 'fecha_inicio', 'fecha_fin', 'recurso', 'usuario']