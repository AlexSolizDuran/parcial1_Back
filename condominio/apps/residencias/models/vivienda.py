from django.db import models
from .propietario import Propietario
from ...admin_condominio.models import Condominio

class Vivienda(models.Model):
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE,related_name='viviendas')
    propietario = models.ManyToManyField(Propietario,through='PropietarioVivienda' )
    nro_vivienda = models.PositiveSmallIntegerField()
    precio_alquiler = models.PositiveBigIntegerField(null=True)
    precio_anticretico = models.PositiveBigIntegerField(null=True)
    superficie = models.PositiveBigIntegerField(null=True)
    estado = models.BooleanField(default=True)
    foto = models.ImageField(upload_to='vivienda/',null=True)
    
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
        
class PropietarioVivienda(models.Model):
    estado = models.BooleanField(default=True)
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE)
    vivienda = models.ForeignKey(Vivienda, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'propietario_vivienda'
        unique_together = ('propietario', 'vivienda')
    


    
    