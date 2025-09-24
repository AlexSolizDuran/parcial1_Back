from django.db import models
from .propietario import Propietario
from ...admin_condominio.models import Condominio



class Vivienda(models.Model):
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE,related_name='viviendas')
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE,related_name='viviendas')
    nro_vivienda = models.PositiveSmallIntegerField()
    precio_alquiler = models.PositiveBigIntegerField(null=True)
    precio_anticretico = models.PositiveBigIntegerField(null=True)
    superfice = models.PositiveBigIntegerField(null=True)
    estado = models.BooleanField(default=True)

    class Meta:
        db_table = 'vivienda'
        
class HistorialDueño(models.Model):
    estado = models.BooleanField(default=True)
    fecha_inicio = models.DateField(null=True)
    fecha_fin = models.DateField(null=True)
    propietario_id = models.PositiveBigIntegerField()
    vivienda = models.ForeignKey(Vivienda, on_delete=models.CASCADE,related_name='historial_dueños')
    
    class Meta:
        db_table = 'historial_dueño'
        
class Contrato(models.Model):
    descripcion = models.TextField()
    fecha_ingreso = models.DateTimeField(null=True)
    fecha_salida = models.DateTimeField(null=True)
    porcentaje_expensa = models.PositiveSmallIntegerField(null=True)
    tipo_renta = models.CharField(max_length=30)
    vivienda = models.ForeignKey(Vivienda, on_delete=models.CASCADE,related_name='contratos')
    class Meta:
        db_table = 'contrato'

    
    