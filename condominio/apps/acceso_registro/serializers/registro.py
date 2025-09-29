from rest_framework import serializers
from ..models import Registro,Seguridad
from ...admin_condominio.models import AdminCondominio,Admin
from ...usuario.models import User,Persona,Rol,RolUsuario
from ...usuario.serializers import UserSerializer




class SeguridadSeriliazer(serializers.ModelSerializer):
    usuario = UserSerializer(write_only=True)
    usuario_detail = UserSerializer(source='usuario',read_only=True)
    condominio = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Seguridad
        fields = ['id','usuario','usuario_detail','condominio','turno','estado']
        
    def create(self, validated_data):
        user = self.context['request'].user
        admin = Admin.objects.filter(usuario=user).first()
        condomininio = AdminCondominio.objects.filter(admin=admin, activo=True).first().condominio
        validated_data['condominio'] = condomininio
        
        usuario_data = validated_data.pop("usuario")
        persona_data = usuario_data.pop("persona")
        roles_data = usuario_data.pop("roles", None)  # quitar roles antes de crear usuario

        # Crear persona
        persona = Persona.objects.create(**persona_data)

        # Crear usuario ligado a persona
        password = usuario_data.pop("password", None)
        usuario = User(persona=persona, **usuario_data)
        if password:
            usuario.set_password(password)
        usuario.save()

        # Asignar roles: si no vienen, asignar rol por defecto
        if not roles_data:
            rol_defecto = Rol.objects.get(nombre="seguridad")
            usuario.roles.set([rol_defecto])
        else:
            usuario.roles.set(roles_data)

        # Crear propietario ligado a usuario
        seguridad = Seguridad.objects.create(usuario=usuario, **validated_data)

        return seguridad 

        

class RegistroSerializer(serializers.ModelSerializer):
    condominio = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Registro
        fields = ['id','ci_persona_entrante',
                  'ci_persona_saliente',
                  'fecha_ingreso',
                  'fecha_salida',
                  'condominio',
                  'vehiculo_id',
                  'seguridad_id',
                  'motivo']
    def create(self, validated_data):
        user = self.context['request'].user
        admin = Admin.objects.filter(usuario=user).first()
        admin_condominio = AdminCondominio.objects.filter(admin=admin, activo=True).first()
        if admin_condominio is None:
            seguridad = Seguridad.objects.filter(usuario=user).first()  # obtener objeto Seguridad del usuario)
        else:
            validated_data['condominio'] = admin_condominio.condominio # asignar condominio automáticamente

        validated_data['condominio'] = seguridad.condominio  # asignar condominio automáticamente
        return super().create(validated_data)