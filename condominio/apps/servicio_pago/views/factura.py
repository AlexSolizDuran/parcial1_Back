from rest_framework import viewsets
from ..models import Factura ,DetalleFactura
from ..serializers import FacturaSerializer , DetalleFacturaSerializer
from rest_framework.permissions import IsAuthenticated




class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer
    permission_classes = [IsAuthenticated]
    
class DetalleFacturaViewSet(viewsets.ModelViewSet):
    queryset = DetalleFactura.objects.all()
    serializer_class = DetalleFacturaSerializer
    permission_classes = [IsAuthenticated]