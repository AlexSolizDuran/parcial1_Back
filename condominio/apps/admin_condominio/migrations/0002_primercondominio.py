from django.db import migrations

def crear_instancia(apps, schema_editor):
    # Obtienes el modelo como estaba en ese momento de la migración
    condominio = apps.get_model('admin_condominio', 'condominio')
    condominio.objects.create(
        nombre="Condominio Central",
        direccion="Av. Siempre Viva 123",
        telefono="70000000",
        QR="qr_condominios/oferta1.jpg",  # Debe existir en MEDIA_ROOT/qr_condominios/
        cantidad_viviendas=20,
    )

class Migration(migrations.Migration):

    dependencies = [
        ('admin_condominio', '0001_initial'),  # depende de la migración inicial
    ]

    operations = [
        migrations.RunPython(crear_instancia),
    ]