from rest_framework import viewsets
from ..models import ExpensaVivienda
from ..serializers import ExpensaViviendaSerializer

class ExpensaViviendaViewSet(viewsets.ModelViewSet):
    queryset = ExpensaVivienda.objects.all()
    serializer_class = ExpensaViviendaSerializer