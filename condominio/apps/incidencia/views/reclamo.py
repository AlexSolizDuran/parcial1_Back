from rest_framework import viewsets

from ..models import Reclamo,Foto
from ..serializers import ReclamoSerializer,FotoSerializer
from rest_framework.permissions import IsAuthenticated



class ReclamoViewSet(viewsets.ModelViewSet):
    queryset = Reclamo.objects.all()
    serializer_class = ReclamoSerializer
    permission_classes = [IsAuthenticated]
    
class FotoViewSet(viewsets.ModelViewSet):
    queryset = Foto.objects.all()
    serializer_class = FotoSerializer
    permission_classes = [IsAuthenticated]