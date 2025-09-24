from rest_framework import viewsets
from ..serializers import NotificacionSerializer
from ..models import Notificacion

class NotificacionViewSet(viewsets.ModelViewSet):
    queryset = Notificacion.objects.all()
    serializer_class = NotificacionSerializer
