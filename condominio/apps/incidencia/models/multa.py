from django.db import models
from ...usuario.models import User

class TipoMulta(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    class Meta:
        db_table = 'tipo_multa'


class Multa(models.Model):
    descripcion = models.TextField()
    estado = models.BooleanField(default=True)
    tipo = models.ForeignKey(TipoMulta, on_delete=models.CASCADE)
    Monto = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        db_table = 'multa'

    
