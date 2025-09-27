from rest_framework import viewsets
from ..models.visitante import Visitante,TipoVisita
from ..serializers.visitante import VisitanteSerializer,TipoVisitaSerializer 
from rest_framework.permissions import IsAuthenticated


class TipoVisitaViewSet(viewsets.ModelViewSet):
    queryset = TipoVisita.objects.all()
    serializer_class = TipoVisitaSerializer
    permission_classes = [IsAuthenticated]

class VisitanteViewSet(viewsets.ModelViewSet):
    queryset = Visitante.objects.all()
    serializer_class = VisitanteSerializer
    permission_classes = [IsAuthenticated]