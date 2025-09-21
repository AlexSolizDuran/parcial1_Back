from django.db import models


class Rol(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "rol"

    def __str__(self):
        return self.nombre
    
class RolUsuario(models.Model):
    #en la db esto se muestra usuario_id
    usuario = models.ForeignKey('User', on_delete=models.CASCADE)
    #en la db esto se muestra rol_id
    rol = models.ForeignKey('Rol', on_delete=models.CASCADE)

    class Meta:
        db_table = "rol_usuario"
        unique_together = ('id_usuario', 'id_rol')

    def __str__(self):
        return f"{self.usuario.username} - {self.rol.nombre}"
    