from django.db import migrations

def crear_instancia(apps, schema_editor):
    # Obtienes el modelo como estaba en ese momento de la migración
    condominio = apps.get_model('admin_condominio', 'Condominio')
    admin = apps.get_model('admin_condominio', 'Admin')
    RolUsuario = apps.get_model('usuario', 'RolUsuario')
    User = apps.get_model('usuario', 'User')
    Rol = apps.get_model('usuario', 'Rol')
    admin_condominio = apps.get_model('admin_condominio', 'AdminCondominio')
    
    admin_role = Rol.objects.get(nombre='admin')
    usuarios_admin = User.objects.filter(rolusuario__rol=admin_role)[:2]
    
    
    condominio1 = condominio.objects.create(
        nombre="Condominio Central",
        direccion="Av. Siempre Viva 123",
        telefono="70000000",
        QR="qr_condominios/oferta1.jpg",  # Debe existir en MEDIA_ROOT/qr_condominios/
        cantidad_viviendas=18,
    )
    
    adusuario1 = admin.objects.create(usuario=usuarios_admin[0])
    adusuario2 = admin.objects.create(usuario=usuarios_admin[1])
    
    admin_condominio.objects.create(admin=adusuario1, condominio=condominio1)
    admin_condominio.objects.create(admin=adusuario2, condominio=condominio1)
    
    
    
    

class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
        ('admin_condominio', '0001_initial'),
        ('usuario', '0003_seeduser')
        # depende de la migración inicial
    ]

    operations = [
        migrations.RunPython(crear_instancia),
    ]