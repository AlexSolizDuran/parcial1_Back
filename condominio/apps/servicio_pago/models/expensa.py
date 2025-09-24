from django.db import models
from ...admin_condominio.models.admin_condominio import Condominio



class TipoExpensa(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    class Meta:
        db_table = 'tipo_expensa'
        
        
class Expensa(models.Model):
    estado = models.BooleanField(default=True)
    fecha_vencimiento = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_expensa = models.ForeignKey(TipoExpensa, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE)
    
    
    class Meta:
        db_table = 'expensa'