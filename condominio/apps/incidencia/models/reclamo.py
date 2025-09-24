from django.db import models
from ...usuario.models import User

class Reclamo(models.Model):
    descripcion = models.TextField()
    estado = models.BooleanField(default=True)
    fecha_resolucion = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        db_table = 'reclamo'



class Foto(models.Model):
    descripcion = models.TextField()
    reclamo = models.ForeignKey(Reclamo, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='reclamos/',null=True, blank=True)
    class Meta:
        db_table = 'foto'