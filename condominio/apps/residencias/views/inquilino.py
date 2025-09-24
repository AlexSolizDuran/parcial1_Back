from rest_framework import viewsets
from ..models import Inquilino,Mascota,Contrato
from ..serializers import InquilinoSerializer,MascotaSerializer,ContratoSerializer

class InquilinoViewSet(viewsets.ModelViewSet):
    queryset = Inquilino.objects.all()
    serializer_class = InquilinoSerializer 
    
class MascotaViewSet(viewsets.ModelViewSet):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer
    
