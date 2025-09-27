from rest_framework import viewsets
from ..models import Rol,RolUsuario
from ..serializers import RolSerializer,RolUsuarioSerializer
from rest_framework.permissions import IsAuthenticated



class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer
    permission_classes = [IsAuthenticated]
    
    
class RolUsuarioViewSet(viewsets.ModelViewSet):
    queryset = RolUsuario.objects.all()
    serializer_class = RolUsuarioSerializer
    permission_classes = [IsAuthenticated]
    

