from rest_framework import viewsets
from ..models.visitante import Visitante,TipoVisita
from ..serializers.visitante import VisitanteSerializer,TipoVisitaSerializer    

class TipoVisitaViewSet(viewsets.ModelViewSet):
    queryset = TipoVisita.objects.all()
    serializer_class = TipoVisitaSerializer

class VisitanteViewSet(viewsets.ModelViewSet):
    queryset = Visitante.objects.all()
    serializer_class = VisitanteSerializer