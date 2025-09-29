from rest_framework import viewsets
from rest_framework import permissions
from ..models import Propietario,Parqueo,NumeroParqueo,PropietarioVivienda
from ..serializers import (PropietarioSerializer,
                           ParqueoSerializer,
                           NumeroParqueoSerializer,
                           PropietarioViviendaSerializer)

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

class PropietarioViewSet(viewsets.ModelViewSet):
    queryset = Propietario.objects.all()
    serializer_class = PropietarioSerializer
    permission_classes = [permissions.AllowAny]
    
    
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
    
    @action(detail=False, methods=["GET"])
    def idpropietario(self, request):
        user = request.user
        propietario = Propietario.objects.get(pk=user.pk)
        serializer = PropietarioSerializer(propietario)
        return Response(serializer.data)
        


    
class ParqueoViewSet(viewsets.ModelViewSet):
    queryset = Parqueo.objects.all()
    serializer_class = ParqueoSerializer
    permission_classes = [IsAuthenticated]
    
class NumeroParqueoViewSet(viewsets.ModelViewSet):
    queryset = NumeroParqueo.objects.all()
    serializer_class = NumeroParqueoSerializer
    permission_classes = [IsAuthenticated]