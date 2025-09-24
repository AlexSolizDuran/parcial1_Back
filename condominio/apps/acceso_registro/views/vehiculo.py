from rest_framework import viewsets
from ..models.vehiculo import Vehiculo
from ..serializers.vehiculo import VehiculoSerializer

class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer