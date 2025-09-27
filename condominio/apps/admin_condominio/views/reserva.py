from rest_framework import viewsets
from ..models import Reserva
from ..serializers import ReservaSerializer
from rest_framework.permissions import IsAuthenticated


class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    permission_classes = [IsAuthenticated]