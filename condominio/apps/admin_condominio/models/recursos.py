from django.db import models
from .admin_condominio import Condominio

class TipoRecurso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "tipo_recurso"

class Recurso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True,blank=True)
    estado = models.BooleanField(default=True)
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE)
    tipo_recurso = models.ForeignKey(TipoRecurso, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "recurso"
        
        
      