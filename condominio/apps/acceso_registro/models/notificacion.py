from django.db import models
from ...usuario.models import User

class Notificacion(models.Model):
    descripcion = models.TextField()
    titulo = models.CharField(max_length=100)
    usuario = models.ForeignKey(User, on_delete = models.CASCADE)
    leido = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'notificacion'
    

    