from rest_framework import viewsets
from ..models import AdminCondominio,Admin,Condominio
from ..serializers import AdminSerializer,AdminCondominioSerializer,CondominioSerializer

class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    
class AdminCondominioViewSet(viewsets.ModelViewSet):
    queryset = AdminCondominio.objects.all()
    serializer_class = AdminCondominioSerializer
    
class CondominioViewSet(viewsets.ModelViewSet):
    queryset = Condominio.objects.all()
    serializer_class = CondominioSerializer