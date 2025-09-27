from rest_framework import viewsets
from ..models import Recurso ,TipoRecurso
from ..serializers import RecursoSerializer,TipoRecursoSerializer
from rest_framework.permissions import IsAuthenticated

class RecursoViewSet(viewsets.ModelViewSet):
    queryset = Recurso.objects.all()
    serializer_class = RecursoSerializer
    permission_classes = [IsAuthenticated]


class TipoRecursoViewSet(viewsets.ModelViewSet):
    queryset = TipoRecurso.objects.all()
    serializer_class = TipoRecursoSerializer
    permission_classes = [IsAuthenticated]