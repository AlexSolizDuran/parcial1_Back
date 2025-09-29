from rest_framework import serializers
from ..models import Propietario, Parqueo, NumeroParqueo
from ...usuario.models import User, Persona,Rol
from ...usuario.serializers import UserSerializer


class PropietarioSerializer(serializers.ModelSerializer):
    usuario = UserSerializer(write_only=True)
    usuario_detail = UserSerializer(source='usuario',read_only=True)
    
    class Meta:
        model = Propietario
        fields = ['id','usuario','usuario_detail', 'estado', 'fecha_compra', 'QRpago']
        
    def create(self, validated_data):
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
            rol_defecto = Rol.objects.get(nombre="propietario")
            usuario.roles.set([rol_defecto])
        else:
            usuario.roles.set(roles_data)

        # Crear propietario ligado a usuario
        propietario = Propietario.objects.create(usuario=usuario, **validated_data)

        return propietario
   
        
class ParqueoSerializer(serializers.ModelSerializer):
    propietario = serializers.PrimaryKeyRelatedField(queryset=Propietario.objects.all())
    class Meta:
        model = Parqueo
        fields = ['id','descripcion', 'propietario']

class NumeroParqueoSerializer(serializers.ModelSerializer):
    parqueo = serializers.PrimaryKeyRelatedField(queryset=Parqueo.objects.all())
    class Meta:
        model = NumeroParqueo
        fields = ['id','inquilino_id', 'parqueo', 'numero']