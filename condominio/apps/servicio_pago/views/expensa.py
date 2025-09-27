from rest_framework import viewsets
from .. models import Expensa,TipoExpensa
from ..serializers import ExpensaSerializer,TipoExpensaSerializer
from rest_framework.permissions import IsAuthenticated


class ExpensaViewSet(viewsets.ModelViewSet):
    queryset = Expensa.objects.all()
    serializer_class = ExpensaSerializer
    permission_classes = [IsAuthenticated]
    
class TipoExpensaViewSet(viewsets.ModelViewSet):
    queryset = TipoExpensa.objects.all()
    serializer_class = TipoExpensaSerializer
    permission_classes = [IsAuthenticated]