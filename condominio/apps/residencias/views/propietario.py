from rest_framework import viewsets
from ..models import Propietario,Parqueo,NumeroParqueo,Vivienda,PropietarioVivienda
from ..serializers import (PropietarioSerializer,
                           ParqueoSerializer,
                           NumeroParqueoSerializer,
                           ViviendaSerializer,
                           PropietarioViviendaSerializer)
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
        
        '''
        viviendas_activas = Vivienda.objects.filter(
            propietariovivienda_set__propietario=propietario,
            propietariovivienda_set__estado=True
        ).prefetch_related(
            'contrato_set',
            'contrato_set__inquilino',
            'contrato_set__ocupante_set'
        )
        '''
        propietario_obj = Propietario.objects.get(usuario=request.user)
        propietario_vivienda = PropietarioVivienda.objects.filter(propietario=propietario_obj)
        serializer = PropietarioViviendaSerializer(propietario_vivienda, many=True)  # many=True aquí está bien
        return Response(serializer.data)


    
class ParqueoViewSet(viewsets.ModelViewSet):
    queryset = Parqueo.objects.all()
    serializer_class = ParqueoSerializer
    permission_classes = [IsAuthenticated]
    
class NumeroParqueoViewSet(viewsets.ModelViewSet):
    queryset = NumeroParqueo.objects.all()
    serializer_class = NumeroParqueoSerializer
    permission_classes = [IsAuthenticated]