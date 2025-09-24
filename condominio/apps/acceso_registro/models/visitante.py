from django.db import models
from ...usuario.models import Persona

class TipoVisita(models.Model):
    nombre = models.CharField(max_length=100)
    class Meta:        
        db_table = 'tipo_visita'

class Visitante(models.Model):
    persona = models.ForeignKey(Persona, on_delete = models.CASCADE)
    tipo_visita = models.ForeignKey(TipoVisita, on_delete = models.CASCADE)
    fecha_visita = models.DateTimeField(null=True)
    estado = models.BooleanField(default=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    motivo = models.TextField()
    class Meta:
        db_table = 'visitante'



    