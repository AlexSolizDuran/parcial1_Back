from rest_framework import viewsets
from ..models import ServicioBasico
from ..serializers import ServicioBasicoSerializer
from rest_framework.permissions import IsAuthenticated



class ServicioBasicoViewSet(viewsets.ModelViewSet):
    queryset = ServicioBasico.objects.all()
    serializer_class = ServicioBasicoSerializer
    permission_classes = [IsAuthenticated]