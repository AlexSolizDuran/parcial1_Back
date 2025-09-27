from django.db import migrations
from faker import Faker

fake = Faker()

def crear_instancia(apps, schema_editor):
    # Obtienes el modelo como estaba en ese momento de la migración
    propietario = apps.get_model('residencias', 'Propietario')
    RolUsuario = apps.get_model('usuario', 'RolUsuario')
    Inquilino = apps.get_model('residencias', 'Inquilino')
    User = apps.get_model('usuario', 'User')
    Rol = apps.get_model('usuario', 'Rol')
    
    propietario_role = Rol.objects.get(nombre='propietario')
    usuarios_propietario = User.objects.filter(rolusuario__rol=propietario_role)[:5]
    
    propietario1 = propietario.objects.create(usuario=usuarios_propietario[0] , fecha_compra=fake.date_between(start_date='-2y', end_date='today'))
    propietario2 = propietario.objects.create(usuario=usuarios_propietario[1],fecha_compra=fake.date_between(start_date='-2y', end_date='today'))
    propietario3 = propietario.objects.create(usuario=usuarios_propietario[2],fecha_compra=fake.date_between(start_date='-2y', end_date='today'))
    propietario3 = propietario.objects.create(usuario=usuarios_propietario[3],fecha_compra=fake.date_between(start_date='-2y', end_date='today'))
    propietario3 = propietario.objects.create(usuario=usuarios_propietario[4],fecha_compra=fake.date_between(start_date='-2y', end_date='today'))

    inquilino_role = Rol.objects.get(nombre='inquilino')
    usuarios_inquilino = User.objects.filter(rolusuario__rol=inquilino_role)[:5]
    
    inquilino1 = Inquilino.objects.create(usuario=usuarios_inquilino[0])
    inquilino2 = Inquilino.objects.create(usuario=usuarios_inquilino[1])
    inquilino3 = Inquilino.objects.create(usuario=usuarios_inquilino[2])
    inquilino4 = Inquilino.objects.create(usuario=usuarios_inquilino[3])
    inquilino5 = Inquilino.objects.create(usuario=usuarios_inquilino[4])
    
    
class Migration(migrations.Migration):

    dependencies = [
        ('residencias', '0003_remove_inquilino_contrato_contrato_inquilino'),
        ('usuario', '0001_initial'),
        ('usuario', '0003_seeduser'),# depende de la migración inicial
    ]

    operations = [
        migrations.RunPython(crear_instancia),
    ]