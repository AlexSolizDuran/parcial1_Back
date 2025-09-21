from rest_framework import viewsets
from ..models import Gasto
from ..serializers import GastoSerializers

class GastoViewSet(viewsets.ModelViewSet):
    queryset = Gasto.objects.all()
    serializer_class = GastoSerializers