from rest_framework import viewsets

from ..models import Multa,TipoMulta
from ..serializers import MultaSerializer,TipoMultaSerializer
from rest_framework.permissions import IsAuthenticated


class MultaViewSet(viewsets.ModelViewSet):
    queryset = Multa.objects.all()
    serializer_class = MultaSerializer 
    permission_classes = [IsAuthenticated]
    
class TipoMultaViewSet(viewsets.ModelViewSet):
    queryset = TipoMulta.objects.all()
    serializer_class = TipoMultaSerializer
    permission_classes = [IsAuthenticated]