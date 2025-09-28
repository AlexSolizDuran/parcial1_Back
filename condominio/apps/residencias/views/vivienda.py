from rest_framework import viewsets
from ..models import Vivienda,HistorialDueño,PropietarioVivienda
from ..serializers import ViviendaSerializer,HistorialDueñoSerializer,PropietarioViviendaSerializer
from rest_framework.permissions import IsAuthenticated



class ViviendaViewSet(viewsets.ModelViewSet):
    queryset = Vivienda.objects.all()
    serializer_class = ViviendaSerializer
    permission_classes = [IsAuthenticated]
    
class HistorialDueñoViewSet(viewsets.ModelViewSet):
    queryset = HistorialDueño.objects.all()
    serializer_class = HistorialDueñoSerializer
    permission_classes = [IsAuthenticated]
    
class PropietarioViviendaViewSet(viewsets.ModelViewSet):
    queryset = PropietarioVivienda.objects.all()
    serializer_class = PropietarioViviendaSerializer
    permission_classes = [IsAuthenticated]
