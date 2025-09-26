from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("El usuario debe tener un username")
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, password, **extra_fields)


class Persona(models.Model):
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    ci = models.CharField(max_length=20, null=True)
    fecha_nacimiento = models.DateField(null=True)
    foto = models.ImageField(upload_to='fotos/', null=True)  
    genero = models.CharField(max_length=10, null=True)
    direccion = models.CharField(max_length=255,  null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "persona"
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    

class User(AbstractBaseUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    #en la db esto se muestra persona_id
    persona = models.OneToOneField('persona', on_delete=models.CASCADE, related_name='usuario')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    activo = models.BooleanField(default=True)
    
    roles = models.ManyToManyField(
        'Rol',
        through='RolUsuario',
        related_name='usuarios'
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']  
    
    class Meta:
        db_table = "usuario"
        
    def __str__(self):
        return self.username
