from django.db import migrations
from faker import Faker

fake = Faker()

def crear_instancia(apps, schema_editor):
    # Obtienes el modelo como estaba en ese momento de la migración
    propietario = apps.get_model('residencias', 'Propietario')
    Vivienda = apps.get_model('residencias', 'Vivienda')
    Inquilino = apps.get_model('residencias', 'Inquilino')
    User = apps.get_model('usuario', 'User')
    Rol = apps.get_model('usuario', 'Rol')
    Condominio = apps.get_model('admin_condominio', 'Condominio')
    Propietario_vivienda = apps.get_model('residencias', 'PropietarioVivienda')
    Contrato = apps.get_model('residencias', 'Contrato')
    Ocupante = apps.get_model('residencias', 'Ocupante')
    Persona = apps.get_model('usuario', 'Persona')
    Seguridad = apps.get_model('acceso_registro', 'Seguridad')
    
    propietario_role = Rol.objects.get(nombre='propietario')
    usuarios_propietario = User.objects.filter(rolusuario__rol=propietario_role)[:5]
    
    propietario1 = propietario.objects.create(usuario=usuarios_propietario[0] , fecha_compra=fake.date_between(start_date='-2y', end_date='today'))
    propietario2 = propietario.objects.create(usuario=usuarios_propietario[1],fecha_compra=fake.date_between(start_date='-2y', end_date='today'))
    propietario3 = propietario.objects.create(usuario=usuarios_propietario[2],fecha_compra=fake.date_between(start_date='-2y', end_date='today'))
    propietario4 = propietario.objects.create(usuario=usuarios_propietario[3],fecha_compra=fake.date_between(start_date='-2y', end_date='today'))
    propietario5 = propietario.objects.create(usuario=usuarios_propietario[4],fecha_compra=fake.date_between(start_date='-2y', end_date='today'))

    inquilino_role = Rol.objects.get(nombre='inquilino')
    usuarios_inquilino = User.objects.filter(rolusuario__rol=inquilino_role)[:5]
    
    inquilino1 = Inquilino.objects.create(usuario=usuarios_inquilino[0])
    inquilino2 = Inquilino.objects.create(usuario=usuarios_inquilino[1])
    inquilino3 = Inquilino.objects.create(usuario=usuarios_inquilino[2])
    inquilino4 = Inquilino.objects.create(usuario=usuarios_inquilino[3])
    inquilino5 = Inquilino.objects.create(usuario=usuarios_inquilino[4])
    
    condominio = Condominio.objects.first()
    
    seguridad_role = Rol.objects.get(nombre='seguridad')
    usuarios_seguridad = User.objects.filter(rolusuario__rol=seguridad_role)[:2]
    seguridad1 = Seguridad.objects.create(usuario=usuarios_seguridad[0], condominio=condominio, turno='Mañana')
    #seguridad2 = Seguridad.objects.create(usuario=usuarios_seguridad[1], condominio=condominio, turno='Tarde')
    

    vivienda1 = Vivienda.objects.create(
        condominio=condominio, 
        nro_vivienda=101,
        precio_alquiler=1001,
        precio_anticretico=50001,
        superficie=100,
        estado=True)
    vivienda2 = Vivienda.objects.create(
        condominio=condominio,
        nro_vivienda=102,
        precio_alquiler=1002,
        precio_anticretico=50002,
        superficie=100,
        estado=True)
    vivienda3 = Vivienda.objects.create(
        condominio=condominio,
        nro_vivienda=103,
        precio_alquiler=1003,
        precio_anticretico=50003,
        superficie=100,
        estado=True)
    vivienda4 = Vivienda.objects.create(
        condominio=condominio,
        nro_vivienda=104,
        precio_alquiler=1004,
        precio_anticretico=50004,
        superficie=100,
        estado=True)
    vivienda5 = Vivienda.objects.create(
        condominio=condominio, 
        nro_vivienda=105,
        precio_alquiler=1005,
        precio_anticretico=50005,
        superficie=100,
        estado=True)
    
    Propietario_vivienda.objects.create(propietario=propietario1, vivienda=vivienda1)
    Propietario_vivienda.objects.create(propietario=propietario1, vivienda=vivienda2)
    Propietario_vivienda.objects.create(propietario=propietario3, vivienda=vivienda3)
    Propietario_vivienda.objects.create(propietario=propietario4, vivienda=vivienda4)
    Propietario_vivienda.objects.create(propietario=propietario5, vivienda=vivienda5)
    
    contrato1 = Contrato.objects.create(descripcion='Contrato 1',
                                        fecha_ingreso=fake.date_between(start_date='-2y', end_date='today'),
                                        fecha_salida=fake.date_between(start_date='-2y', end_date='today'),
                                        porcentaje_expensa=10,
                                        tipo_renta='Alquiler',
                                        vivienda=vivienda1,
                                        inquilino=inquilino1)
    contrato2 = Contrato.objects.create(descripcion='Contrato 2',
                                        fecha_ingreso=fake.date_between(start_date='-2y', end_date='today'),
                                        fecha_salida=fake.date_between(start_date='-2y', end_date='today'),
                                        porcentaje_expensa=10,
                                        tipo_renta='Alquiler',
                                        vivienda=vivienda2,
                                        inquilino=inquilino2)
    contrato3 = Contrato.objects.create(descripcion='Contrato 3',
                                        fecha_ingreso=fake.date_between(start_date='-2y', end_date='today'),
                                        fecha_salida=fake.date_between(start_date='-2y', end_date='today'),
                                        porcentaje_expensa=10,
                                        tipo_renta='Alquiler',
                                        vivienda=vivienda3,
                                        inquilino=inquilino3)
    contrato4 = Contrato.objects.create(descripcion='Contrato 4',
                                        fecha_ingreso=fake.date_between(start_date='-2y', end_date='today'),
                                        fecha_salida=fake.date_between(start_date='-2y', end_date='today'),
                                        porcentaje_expensa=10,
                                        tipo_renta='Alquiler',
                                        vivienda=vivienda4,
                                        inquilino=inquilino4)
    contrato5 = Contrato.objects.create(descripcion='Contrato 5',
                                        fecha_ingreso=fake.date_between(start_date='-2y', end_date='today'),
                                        fecha_salida=fake.date_between(start_date='-2y', end_date='today'),
                                        porcentaje_expensa=10,
                                        tipo_renta='Alquiler',
                                        vivienda=vivienda5,
                                        inquilino=inquilino5)
    
    persona = Persona.objects.exclude(usuario__isnull=True)[:10]
    ocupante1 = Ocupante.objects.create(persona_ci=persona[0].ci, estado=True, contrato=contrato1)
    ocupante2 = Ocupante.objects.create(persona_ci=persona[1].ci, estado=True, contrato=contrato1)
    ocupante3 = Ocupante.objects.create(persona_ci=persona[2].ci, estado=True,contrato=contrato2)
    ocupante4 = Ocupante.objects.create(persona_ci=persona[3].ci, estado=True,contrato=contrato2)
    ocupante5 = Ocupante.objects.create(persona_ci=persona[4].ci, estado=True,contrato=contrato3)
    ocupante6 = Ocupante.objects.create(persona_ci=persona[5].ci, estado=True,contrato=contrato3)
    ocupante7 = Ocupante.objects.create(persona_ci=persona[6].ci, estado=True,contrato=contrato4)
    ocupante8 = Ocupante.objects.create(persona_ci=persona[7].ci, estado=True,contrato=contrato4)
    ocupante9 = Ocupante.objects.create(persona_ci=persona[8].ci, estado=True,contrato=contrato5)
    ocupante10 = Ocupante.objects.create(persona_ci=persona[9].ci, estado=True,contrato=contrato5)
    

    
    seguridad_role = Rol.objects.get(nombre='seguridad')
    
   
    

    
    
class Migration(migrations.Migration):

    dependencies = [
        ('residencias', '0001_initial'),
        ('usuario', '0001_initial'),
        ('usuario', '0003_seeduser'),
        ('acceso_registro', '0001_initial'),
        ('admin_condominio', '0001_initial')
        
        
    ]

    operations = [
        migrations.RunPython(crear_instancia),
    ]