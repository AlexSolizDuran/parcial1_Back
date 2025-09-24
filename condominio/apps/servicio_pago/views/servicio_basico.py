from rest_framework import viewsets
from ..models import ServicioBasico
from ..serializers import ServicioBasicoSerializer

class ServicioBasicoViewSet(viewsets.ModelViewSet):
    queryset = ServicioBasico.objects.all()
    serializer_class = ServicioBasicoSerializer