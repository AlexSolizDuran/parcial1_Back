from django.db import migrations
from django.utils import timezone
from faker import Faker
from django.contrib.auth.hashers import make_password
import random

fake = Faker()

def crear_usuarios_con_roles(apps, schema_editor):
    Persona = apps.get_model('usuario', 'Persona')
    User = apps.get_model('usuario', 'User')
    Rol = apps.get_model('usuario', 'Rol')
    RolUsuario = apps.get_model('usuario', 'RolUsuario')

    # Crear roles base si no existen
    roles_nombres = ["admin", "propietario","inquilino","seguridad"]
    roles = []
    for nombre in roles_nombres:
        rol, _ = Rol.objects.get_or_create(nombre=nombre, defaults={'descripcion': f'Rol {nombre}'})
        roles.append(rol)

    for i in range(12):
        # Crear persona
        persona = Persona.objects.create(
            nombre=fake.first_name(),
            apellido=fake.last_name(),
            ci=str(fake.random_number(digits=8)),
            fecha_nacimiento=fake.date_of_birth(minimum_age=18, maximum_age=65),
            genero=random.choice(["M", "F","N"]),
            direccion=fake.address(),
            telefono=fake.numerify(text="#######")
        )

        # Crear usuario
        username = f"user{i+1}"
        user = User.objects.create(
            username=username,
            email=f"{username}@example.com",
            persona=persona,
             password=make_password("123456"),
            activo=True,
            created_at=timezone.now(),
            updated_at=timezone.now()
        )
        user.save()

        # Asignar 1 o 2 roles aleatorios
        if i == 0:
            asignados = [roles[0]]
        elif i == 2:
            asignados = [roles[1]]
        elif i == 7:
            asignados = [roles[2]]
       
        for rol in asignados:
            RolUsuario.objects.create(usuario=user, rol=rol)
    
    for i in range(10):
        persona = Persona.objects.create(
            nombre=fake.first_name(),
            apellido=fake.last_name(),
            ci=str(fake.random_number(digits=8)),
            genero=random.choice(["M", "F"]),
            fecha_nacimiento=fake.date_of_birth(minimum_age=18, maximum_age=65),
            direccion=fake.address(),
            telefono=fake.numerify(text="#######")
        )
        
       

class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(crear_usuarios_con_roles),
    ]
