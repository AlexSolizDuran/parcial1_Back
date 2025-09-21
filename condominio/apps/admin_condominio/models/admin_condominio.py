from django.db import models
from ...usuario.models import User

class Admin(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)
    created_ad = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "admin"

class Condominio(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    QR = models.ImageField(upload_to='qr_condominios/')
    cantidad_viviendas = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    admin = models.ManyToManyField(Admin,through='AdminCondominio')

    class Meta:
        db_table = "condominio"


class AdminCondominio(models.Model):
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "admin_condominio"
        unique_together = ('admin', 'condominio')


    