from rest_framework import viewsets
from ..models import Pago,TipoPago
from ..serializers import PagoSerializer,TipoPagoSerializer
from rest_framework.permissions import IsAuthenticated



class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer
    permission_classes = [IsAuthenticated]
    

class TipoPagoViewSet(viewsets.ModelViewSet):
    queryset = TipoPago.objects.all()
    serializer_class = TipoPagoSerializer
    permission_classes = [IsAuthenticated]