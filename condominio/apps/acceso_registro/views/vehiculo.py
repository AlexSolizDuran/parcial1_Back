from rest_framework import viewsets
from ..models.vehiculo import Vehiculo
from ..serializers.vehiculo import VehiculoSerializer
from rest_framework.permissions import IsAuthenticated

class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer
    permission_classes = [IsAuthenticated]

    