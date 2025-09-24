from rest_framework import viewsets

from ..models import Reclamo,Foto
from ..serializers import ReclamoSerializer,FotoSerializer

class ReclamoViewSet(viewsets.ModelViewSet):
    queryset = Reclamo.objects.all()
    serializer_class = ReclamoSerializer
    
class FotoViewSet(viewsets.ModelViewSet):
    queryset = Foto.objects.all()
    serializer_class = FotoSerializer