from rest_framework import viewsets
from ..models import AdminCondominio,Admin,Condominio
from ..serializers import AdminSerializer,AdminCondominioSerializer,CondominioSerializer
from rest_framework.permissions import IsAuthenticated


class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    permission_classes = [IsAuthenticated]
    
class AdminCondominioViewSet(viewsets.ModelViewSet):
    queryset = AdminCondominio.objects.all()
    serializer_class = AdminCondominioSerializer
    permission_classes = [IsAuthenticated]


class CondominioViewSet(viewsets.ModelViewSet):
    queryset = Condominio.objects.all()
    serializer_class = CondominioSerializer
    permission_classes = [IsAuthenticated]