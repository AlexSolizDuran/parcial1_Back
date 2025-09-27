from rest_framework import viewsets
from ..models import NotaAlquiler
from ..serializers import NotaAlquilerSerializer
from rest_framework.permissions import IsAuthenticated



class NotaAlquilerViewSet(viewsets.ModelViewSet):
    queryset = NotaAlquiler.objects.all()
    serializer_class = NotaAlquilerSerializer
    permission_classes = [IsAuthenticated]