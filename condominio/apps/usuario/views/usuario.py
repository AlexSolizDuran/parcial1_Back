from rest_framework import viewsets
from ..serializers import UserSerializer,PersonaSerializer,UserListSerializer
from ..models import User,Persona
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return super().get_queryset().exclude(roles__nombre="admin")
    
    
    

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        queryset = super().get_queryset()

        # Obtener el pk de la URL
        pk = self.kwargs.get("pk")
        if pk:
            # Si se pide un detalle, devolver esa persona sin filtrar
            return queryset.filter(pk=pk)

        # Si es listado, aplicar filtro de usuario nulo
        return queryset.filter(usuario__isnull=True)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.foto:
            instance.foto.delete(save=False)
        return super().destroy(request, *args, **kwargs)