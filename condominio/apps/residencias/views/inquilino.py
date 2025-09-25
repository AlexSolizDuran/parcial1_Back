from rest_framework import viewsets
from ..models import Inquilino,Mascota,Ocupante
from ..serializers import InquilinoSerializer,MascotaSerializer,OcupanteSerializer

class InquilinoViewSet(viewsets.ModelViewSet):
    queryset = Inquilino.objects.all()
    serializer_class = InquilinoSerializer 
    
class MascotaViewSet(viewsets.ModelViewSet):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer
    
class OcupanteViewSet(viewsets.ModelViewSet):
    queryset = Ocupante.objects.all()
    serializer_class = OcupanteSerializer   