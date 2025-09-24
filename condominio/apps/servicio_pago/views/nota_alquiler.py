from rest_framework import viewsets
from ..models import NotaAlquiler
from ..serializers import NotaAlquilerSerializer

class NotaAlquilerViewSet(viewsets.ModelViewSet):
    queryset = NotaAlquiler.objects.all()
    serializer_class = NotaAlquilerSerializer