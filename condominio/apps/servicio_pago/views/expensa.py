from rest_framework import viewsets
from .. models import Expensa,TipoExpensa
from ..serializers import ExpensaSerializer,TipoExpensaSerializer

class ExpensaViewSet(viewsets.ModelViewSet):
    queryset = Expensa.objects.all()
    serializer_class = ExpensaSerializer
    
class TipoExpensaViewSet(viewsets.ModelViewSet):
    queryset = TipoExpensa.objects.all()
    serializer_class = TipoExpensaSerializer