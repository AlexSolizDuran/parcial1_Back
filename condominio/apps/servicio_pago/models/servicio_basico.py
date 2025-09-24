from django.db import models
from ...residencias.models.vivienda import Vivienda


class ServicioBasico(models.Model):
    nombre_empresa = models.CharField(max_length=100)
    numero_Factura = models.PositiveBigIntegerField()
    descripcion = models.TextField()
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_fin = models.DateField()
    fecha_inicio = models.DateField()
    vivienda = models.ForeignKey(Vivienda, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='servicio_basico_images/',null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'servicio_basico'