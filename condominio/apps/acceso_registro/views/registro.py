from rest_framework import viewsets
from ..models.registro import Registro, Seguridad
from ..serializers.registro import RegistroSerializer,SeguridadSeriliazer
from rest_framework.permissions import IsAuthenticated


class RegistroViewSet(viewsets.ModelViewSet):
    queryset = Registro.objects.all()
    serializer_class = RegistroSerializer
    permission_classes = [IsAuthenticated]


class SeguridadViewSet(viewsets.ModelViewSet):
    queryset = Seguridad.objects.all()
    serializer_class = SeguridadSeriliazer
    permission_classes = [IsAuthenticated]