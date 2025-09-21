from rest_framework import viewsets
from ..models import AdminCondominio,Admin
from ..serializers import AdminSerializer,AdminCondominioSerializer

class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    
class AdminCondominioViewSet(viewsets.ModelViewSet):
    queryset = AdminCondominio.objects.all()
    serializer_Class = AdminCondominioSerializer