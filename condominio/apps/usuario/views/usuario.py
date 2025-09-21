from rest_framework import viewsets
from ..serializers import UserSerializer,PersonaSerializer
from ..models import User,Persona
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer