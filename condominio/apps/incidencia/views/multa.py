from rest_framework import viewsets

from ..models import Multa,TipoMulta
from ..serializers import MultaSerializer,TipoMultaSerializer

class MultaViewSet(viewsets.ModelViewSet):
    queryset = Multa.objects.all()
    serializer_class = MultaSerializer 
    
class TipoMultaViewSet(viewsets.ModelViewSet):
    queryset = TipoMulta.objects.all()
    serializer_class = TipoMultaSerializer