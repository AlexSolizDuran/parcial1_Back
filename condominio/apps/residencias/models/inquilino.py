from django.db import models
from ...usuario.models import User
from .vivienda import Vivienda

class Inquilino(models.Model):
    estado = models.BooleanField(default=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'inquilino'
    
    def delete(self, *args, **kwargs):
        if self.usuario:
            self.usuario.delete()  # esto también borrará la persona si el FK de User usa CASCADE
        super().delete(*args, **kwargs)
   
            
class Mascota(models.Model):
    nombre = models.CharField(max_length=50)
    especie = models.CharField(max_length=50)
    raza = models.CharField(max_length=50, null=True, blank=True)
    inquilino = models.ForeignKey(Inquilino, on_delete=models.CASCADE, related_name='mascotas')
    
    class Meta:
        db_table = 'mascota'
        
  
class Contrato(models.Model):
    descripcion = models.TextField()
    fecha_ingreso = models.DateTimeField(null=True)
    fecha_salida = models.DateTimeField(null=True)
    inquilino = models.ForeignKey(Inquilino, on_delete=models.CASCADE,null=True)
    porcentaje_expensa = models.PositiveSmallIntegerField(null=True)
    tipo_renta = models.CharField(max_length=30)
    vivienda = models.ForeignKey(Vivienda, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'contrato'


class Ocupante(models.Model):
    persona_ci = models.PositiveBigIntegerField()
    estado = models.BooleanField(default=True)
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE,related_name='ocupantes',null=True)
    class Meta:
        db_table = 'ocupante'