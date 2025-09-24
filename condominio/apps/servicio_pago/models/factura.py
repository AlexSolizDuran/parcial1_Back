from django.db import models
from ...usuario.models import User
class Factura(models.Model):
    nro_factura = models.PositiveBigIntegerField()
    descripcion = models.TextField()
    fecha_emision = models.DateField()
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.BooleanField(default=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        db_table = 'factura'


class DetalleFactura(models.Model):
    descripcion = models.TextField(null=True, blank=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'detalle_factura'