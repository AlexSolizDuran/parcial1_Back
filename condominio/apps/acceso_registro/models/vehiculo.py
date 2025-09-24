from django.db import models
from ...usuario.models import Persona

class Vehiculo(models.Model):
    color = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    placa = models.CharField(max_length=50)
    descripcion = models.TextField(null=True)
    persona = models.ForeignKey(Persona, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'vehiculo'