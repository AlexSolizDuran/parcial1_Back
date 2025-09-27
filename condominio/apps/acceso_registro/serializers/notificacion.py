from rest_framework import serializers
from ..models.notificacion  import Notificacion
from ...usuario.models import User


class NotificacionSerializer(serializers.ModelSerializer):
    usuario = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = Notificacion
        fields = ['id','descripcion','leido','titulo','usuario']