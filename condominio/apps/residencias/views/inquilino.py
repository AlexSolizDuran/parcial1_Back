from rest_framework import viewsets
from ..models import Inquilino,Mascota,Ocupante,Contrato
from ..serializers import InquilinoSerializer,MascotaSerializer,OcupanteSerializer,ContratoSerializer
from rest_framework.permissions import IsAuthenticated


class InquilinoViewSet(viewsets.ModelViewSet):
    queryset = Inquilino.objects.all()
    serializer_class = InquilinoSerializer 
    permission_classes = [IsAuthenticated]
    
class MascotaViewSet(viewsets.ModelViewSet):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer
    permission_classes = [IsAuthenticated]

class ContratoViewSet(viewsets.ModelViewSet):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer
    permission_classes = [IsAuthenticated]
    
class OcupanteViewSet(viewsets.ModelViewSet):
    queryset = Ocupante.objects.all()
    serializer_class = OcupanteSerializer   
    permission_classes = [IsAuthenticated]