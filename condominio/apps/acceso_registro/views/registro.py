from rest_framework import viewsets
from ..models.registro import Registro, Seguridad
from ..serializers.registro import RegistroSerializer,SeguridadSeriliazer


class RegistroViewSet(viewsets.ModelViewSet):
    queryset = Registro.objects.all()
    serializer_class = RegistroSerializer

class SeguridadViewSet(viewsets.ModelViewSet):
    queryset = Seguridad.objects.all()
    serializer_class = SeguridadSeriliazer