from django.db import models
from ...residencias.models.vivienda import Vivienda


class ExpensaVivienda(models.Model):
    fecha_emision = models.DateField()
    fecha_vencimiento = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.BooleanField(default=False)
    vivienda = models.ForeignKey(Vivienda, on_delete=models.CASCADE)
    expensa_id = models.PositiveBigIntegerField()


    class Meta:
        db_table = 'expensa_vivienda'
