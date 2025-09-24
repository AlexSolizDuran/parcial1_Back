from django.db import models
from .factura import Factura

class TipoPago(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    class Meta:
        db_table = 'tipo_pago'

class Pago(models.Model):
    fecha_pago = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_pago = models.ForeignKey(TipoPago, on_delete=models.CASCADE)
    factura = models.OneToOneField(Factura, on_delete=models.CASCADE)

    class Meta:
        db_table = 'pago'