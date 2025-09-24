from django.db import models
from ...usuario.models import User
from .vivienda import Contrato

class Inquilino(models.Model):
    estado = models.BooleanField(default=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE,related_name='inquilino')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'inquilino'
        
class Mascota(models.Model):
    nombre = models.CharField(max_length=50)
    especie = models.CharField(max_length=50)
    raza = models.CharField(max_length=50, null=True, blank=True)
    inquilino = models.ForeignKey(Inquilino, on_delete=models.CASCADE, related_name='mascotas')
    
    class Meta:
        db_table = 'mascota'