from django.db import models
from ...residencias.models.inquilino import Inquilino
class NotaAlquiler(models.Model):
    fecha_emision = models.DateField()
    fecha_pago = models.DateField()
    monto_alquiler = models.DecimalField(max_digits=10, decimal_places=2)
    monto_otros = models.DecimalField(max_digits=10, decimal_places=2)

    estado = models.BooleanField(default=True)
    inquilino = models.ForeignKey(Inquilino, on_delete=models.CASCADE)

    class Meta:
        db_table = 'nota_alquiler'
        