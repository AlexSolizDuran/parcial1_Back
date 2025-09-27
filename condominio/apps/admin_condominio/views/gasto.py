from rest_framework import viewsets
from ..models import Gasto
from ..serializers import GastoSerializers
from rest_framework.permissions import IsAuthenticated



class GastoViewSet(viewsets.ModelViewSet):
    queryset = Gasto.objects.all()
    serializer_class = GastoSerializers