from django.db import models
from .recursos import Recurso
from ...usuario.models import User


class Reserva(models.Model):
    descripcion = models.TextField()
    estado = models.BooleanField(default=True)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    recurso = models.ForeignKey(Recurso, on_delete=models.CASCADE)
    Usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "reserva"
        