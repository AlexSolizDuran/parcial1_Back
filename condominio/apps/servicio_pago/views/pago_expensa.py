from rest_framework import viewsets
from ..models import ExpensaVivienda
from ..serializers import ExpensaViviendaSerializer
from rest_framework.permissions import IsAuthenticated



class ExpensaViviendaViewSet(viewsets.ModelViewSet):
    queryset = ExpensaVivienda.objects.all()
    serializer_class = ExpensaViviendaSerializer
    permission_classes = [IsAuthenticated]