from django.db import models
from ...usuario.models import User


class Propietario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)
    fecha_compra = models.DateField()
    QRpago = models.ImageField(upload_to='qrpago/',null=True)
    
    created_app = models.DateTimeField(auto_now_add=True)
    updated_app = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'propietario'
        
    def delete(self, *args, **kwargs):
        if self.usuario:
            self.usuario.delete()  # esto también borrará la persona si el FK de User usa CASCADE
        super().delete(*args, **kwargs)
        

class Parqueo(models.Model):
    descripcion = models.TextField()
    propietario = models.OneToOneField(Propietario,on_delete=models.CASCADE)
    class Meta:
        db_table = 'parqueo'    
    
class NumeroParqueo(models.Model):
    inquilino_id = models.PositiveBigIntegerField(null =True)
    parqueo = models.ForeignKey(Parqueo,on_delete=models.CASCADE)
    numero = models.PositiveSmallIntegerField()
    class Meta:
        db_table = 'numero_parqueo'