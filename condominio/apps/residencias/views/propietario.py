from rest_framework import viewsets
from ..models import Propietario,Parqueo,NumeroParqueo,Vivienda
from ..serializers import PropietarioSerializer,ParqueoSerializer,NumeroParqueoSerializer,ViviendaSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from django.db.models import Prefetch
from rest_framework.response import Response

class PropietarioViewSet(viewsets.ModelViewSet):
    queryset = Propietario.objects.all()
    serializer_class = PropietarioSerializer
    permission_classes = [IsAuthenticated]
    
    @action(detail=False, methods=["GET"])
    def misviviendas(self, request):
        usuario = request.user
        propietario = Propietario.objects.get(usuario=usuario)

        viviendas_activas = Vivienda.objects.filter(
            propietariovivienda__propietario=propietario,
            propietariovivienda__estado=True
        ).prefetch_related(
            'contrato_set',
            'contrato_set__inquilino',
            'contrato_set__ocupante_set'
        )

        serializer = ViviendaSerializer(viviendas_activas, many=True)
        return Response(serializer.data)
    
class ParqueoViewSet(viewsets.ModelViewSet):
    queryset = Parqueo.objects.all()
    serializer_class = ParqueoSerializer
    permission_classes = [IsAuthenticated]
    
class NumeroParqueoViewSet(viewsets.ModelViewSet):
    queryset = NumeroParqueo.objects.all()
    serializer_class = NumeroParqueoSerializer
    permission_classes = [IsAuthenticated]