from rest_framework import viewsets
from ..models import Vivienda,HistorialDueño,PropietarioVivienda
from ..serializers import ViviendaSerializer,HistorialDueñoSerializer,PropietarioViviendaSerializer,ViviendaBusquedaSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import filters




class ViviendaViewSet(viewsets.ModelViewSet):
    queryset = Vivienda.objects.all()
    serializer_class = ViviendaSerializer
    permission_classes = [IsAuthenticated]
    
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    
    # Campos que DRF usará para buscar cuando reciba ?search=termino
    # Esto permite buscar por número de vivienda o superficie.
    search_fields = ['nro_vivienda', 'superficie'] 
    
    # Campos permitidos para ordenar
    ordering_fields = ['nro_vivienda', 'superficie', 'id']
    @action(detail=False, methods=['get'])
    def search_list(self, request):
        """
        Endpoint que permite buscar viviendas por número o superficie
        y devuelve una respuesta simplificada para el componente SelectSearch.
        
        URL de uso: /residencias/viviendas/search_list/?search=...
        """
        # Obtener el QuerySet base
        queryset = self.get_queryset()
        
        # Aplicar filtros (SearchFilter, OrderingFilter, etc.) al QuerySet
        queryset = self.filter_queryset(queryset) 
        
        # Aplicar paginación al QuerySet filtrado
        page = self.paginate_queryset(queryset)
        
        # Si la paginación está activada y hay resultados
        if page is not None:
            # Usar el Serializer de búsqueda para devolver datos ligeros
            serializer = ViviendaBusquedaSerializer(page, many=True) 
            return self.get_paginated_response(serializer.data)

        # Si no hay paginación (o si es un listado pequeño)
        serializer = ViviendaBusquedaSerializer(queryset, many=True)
        return Response(serializer.data)
    
class HistorialDueñoViewSet(viewsets.ModelViewSet):
    queryset = HistorialDueño.objects.all()
    serializer_class = HistorialDueñoSerializer
    permission_classes = [IsAuthenticated]
    
class PropietarioViviendaViewSet(viewsets.ModelViewSet):
    queryset = PropietarioVivienda.objects.all()
    serializer_class = PropietarioViviendaSerializer
    permission_classes = [IsAuthenticated]
