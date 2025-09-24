from rest_framework import viewsets
from ..models import Propietario,Parqueo,NumeroParqueo
from ..serializers import PropietarioSerializer,ParqueoSerializer,NumeroParqueoSerializer

class PropietarioViewSet(viewsets.ModelViewSet):
    queryset = Propietario.objects.all()
    serializer_class = PropietarioSerializer
    
class ParqueoViewSet(viewsets.ModelViewSet):
    queryset = Parqueo.objects.all()
    serializer_class = ParqueoSerializer
    
class NumeroParqueoViewSet(viewsets.ModelViewSet):
    queryset = NumeroParqueo.objects.all()
    serializer_class = NumeroParqueoSerializer