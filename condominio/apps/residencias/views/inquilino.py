from rest_framework import viewsets
from ..models import Inquilino,Mascota,Ocupante,Contrato
from ..serializers import (InquilinoSerializer,
                           MascotaSerializer,
                           OcupanteSerializer,
                           ContratoSerializer,
                           ContratoDetallesSerializer,InquilinoBusquedaSerializer)
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework import filters
from ..models.propietario import Propietario
from ..models.vivienda import Vivienda, PropietarioVivienda
from ..models.inquilino import Inquilino, Contrato

class InquilinoViewSet(viewsets.ModelViewSet):
    queryset = Inquilino.objects.all()
    serializer_class = InquilinoSerializer 
    #permission_classes = [IsAuthenticated]
    permission_classes = [permissions.AllowAny] 
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    
    # 💡 2. Campos para buscar (ej. por nombre, apellido o CI)
    search_fields = ['usuario__persona__nombre', 'usuario__persona__apellido', 'usuario__persona__ci']
    
    # 💡 3. Campos que permiten ordenar (útil para SelectSearch)
    ordering_fields = ['usuario__persona__nombre', 'usuario__persona__apellido', 'id']
    ordering = ['usuario__persona__nombre'] # Orden por defecto
    
    @action(detail=False, methods=['get'])
    def search_list(self, request):
        # Usar el queryset principal con la precarga
        queryset = self.get_queryset() 
        
        # Aplicar filtros de búsqueda
        queryset = self.filter_queryset(queryset) 
        
        # Aplicar paginación
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = InquilinoBusquedaSerializer(page, many=True) # Usar el Serializer ligero
            return self.get_paginated_response(serializer.data)

        serializer = InquilinoBusquedaSerializer(queryset, many=True)
        return Response(serializer.data)
    #aquie esta la peticion para obtener el contratos
    @action(detail=False, methods=["GET"])
    def micontrato(self, request):
        usuario = request.user
        inquilino = Inquilino.objects.get(usuario=usuario)
        contrato = Contrato.objects.filter(inquilino=inquilino ,estado=True)
        serializer = ContratoSerializer(contrato, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['GET'], url_path="qrpago")
    def qrpago(self, request):
        username = request.query_params.get("username")
        if not username:
            return Response({"error": "Debe enviar ?username="}, status=status.HTTP_400_BAD_REQUEST)
        try:
            propietarios = Propietario.objects.filter(
                propietariovivienda__vivienda__contrato__inquilino__usuario__username=username,
                propietariovivienda__estado=True,
            ).values('id', 'usuario', 'usuario__persona__nombre', 'usuario__persona__apellido', 
                     'estado', 'fecha_compra', 'QRpago')

            return Response(list(propietarios), status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    
    
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
    
    filter_backends = [filters.SearchFilter]
    # DRF buscará en estos campos cuando reciba ?search=termino
    search_fields = ['usuario__persona__nombre', 'usuario__persona__apellido', 'usuario__persona__ci'] 