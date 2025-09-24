from rest_framework import viewsets
from ..models import Vivienda,HistorialDueño,Contrato
from ..serializers import ViviendaSerializer,HistorialDueñoSerializer,ContratoSerializer

class ViviendaViewSet(viewsets.ModelViewSet):
    queryset = Vivienda.objects.all()
    serializer_class = ViviendaSerializer
    
class HistorialDueñoViewSet(viewsets.ModelViewSet):
    queryset = HistorialDueño.objects.all()
    serializer_class = HistorialDueñoSerializer
    
class ContratoViewSet(viewsets.ModelViewSet):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer