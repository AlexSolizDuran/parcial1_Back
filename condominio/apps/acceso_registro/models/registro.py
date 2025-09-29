from django.db import models
from ...admin_condominio.models import Condominio
from ...usuario.models import User


class Registro(models.Model):
    ci_persona_entrante = models.PositiveIntegerField(null=True)
    ci_persona_saliente = models.IntegerField(null=True)
    fecha_ingreso = models.DateTimeField()
    fecha_salida = models.DateTimeField()
    condominio = models.ForeignKey(Condominio, on_delete = models.CASCADE)
    vehiculo_id = models.PositiveIntegerField(null=True)
    motivo = models.TextField()
    seguridad_id = models.PositiveIntegerField(null=True)
    class Meta:
        db_table = 'registro'
    
class Seguridad(models.Model):
    usuario = models.ForeignKey(User, on_delete = models.CASCADE)
    condominio = models.ForeignKey(Condominio, on_delete = models.CASCADE)
    turno = models.CharField(max_length=10)
    estado = models.BooleanField(default=True)
    class Meta:
        db_table = 'seguridad'  
        