from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from ..models import Reclamo,Foto
from ..serializers import ReclamoSerializer,FotoSerializer
from rest_framework.permissions import IsAuthenticated



class ReclamoViewSet(viewsets.ModelViewSet):
    queryset = Reclamo.objects.all()
    serializer_class = ReclamoSerializer
    permission_classes = [IsAuthenticated]

    #GET /incidencia/reclamo/mis_reclamos/
    @action(detail=False, methods=['GET'])
    def mis_reclamos(self, request):
        usuario = request.user
        reclamos = Reclamo.objects.filter(usuario=usuario)
        serializer = self.get_serializer(reclamos, many=True)
        return Response(serializer.data)
    

    
class FotoViewSet(viewsets.ModelViewSet):
    queryset = Foto.objects.all()
    serializer_class = FotoSerializer
    permission_classes = [IsAuthenticated]