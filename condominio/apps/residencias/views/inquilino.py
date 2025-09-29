from rest_framework import viewsets
from ..models import Inquilino,Mascota,Ocupante,Contrato
from ..serializers import (InquilinoSerializer,
                           MascotaSerializer,
                           OcupanteSerializer,
                           ContratoSerializer,
                           ContratoDetallesSerializer)
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions


class InquilinoViewSet(viewsets.ModelViewSet):
    queryset = Inquilino.objects.all()
    serializer_class = InquilinoSerializer 
    permission_classes = [IsAuthenticated]
    
class MascotaViewSet(viewsets.ModelViewSet):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer
    permission_classes = [IsAuthenticated]

class ContratoViewSet(viewsets.ModelViewSet):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer
    permission_classes = [permissions.AllowAny]  
    
    @action(detail=True, methods=["GET"])
    def micontrato(self, request, pk=None):
        
        contrato = self.get_object()
        ocupantes = contrato.ocupantes.all()
        
        response_data = ContratoDetallesSerializer({
            'contrato': contrato, 
            'ocupantes': ocupantes,
        }).data
        
        return Response(response_data, status=status.HTTP_200_OK)
        
    
class OcupanteViewSet(viewsets.ModelViewSet):
    queryset = Ocupante.objects.all()
    serializer_class = OcupanteSerializer   
    permission_classes = [IsAuthenticated]