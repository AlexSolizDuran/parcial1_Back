from rest_framework import viewsets
from ..models import Propietario,Parqueo,NumeroParqueo
from ..serializers import PropietarioSerializer,ParqueoSerializer,NumeroParqueoSerializer
from rest_framework.permissions import IsAuthenticated


class PropietarioViewSet(viewsets.ModelViewSet):
    queryset = Propietario.objects.all()
    serializer_class = PropietarioSerializer
    permission_classes = [IsAuthenticated]
    
class ParqueoViewSet(viewsets.ModelViewSet):
    queryset = Parqueo.objects.all()
    serializer_class = ParqueoSerializer
    permission_classes = [IsAuthenticated]
    
class NumeroParqueoViewSet(viewsets.ModelViewSet):
    queryset = NumeroParqueo.objects.all()
    serializer_class = NumeroParqueoSerializer
    permission_classes = [IsAuthenticated]