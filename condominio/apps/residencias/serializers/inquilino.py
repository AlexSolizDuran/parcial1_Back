from rest_framework import serializers
from ..models import Inquilino,Mascota,Contrato,Ocupante,Vivienda
from ...usuario.models import User,Persona,Rol
from ...usuario.serializers import UserSerializer,PersonaSerializer
from .vivienda import ViviendaSerializer


# serializers.py (Define los datos MINIMOS que necesita el SelectSearch)

class InquilinoBusquedaSerializer(serializers.ModelSerializer):
    # SerializerMethodField para combinar Nombre y Apellido en un solo campo
    display_name = serializers.SerializerMethodField()
    ci = serializers.CharField(source='usuario.persona.ci') # Muestra el CI
    
    class Meta:
        model = Inquilino
        # Solo ID (necesario para el FK), Nombre completo y CI
        fields = ['id', 'display_name', 'ci'] 

    def get_display_name(self, obj):
        # Combina el nombre y apellido para mostrarlo en el frontend
        nombre = obj.usuario.persona.nombre
        apellido = obj.usuario.persona.apellido
        return f"{nombre} {apellido}"
    
class InquilinoSerializer(serializers.ModelSerializer):
    usuario = UserSerializer(write_only=True)
    usuario_detail = UserSerializer(source='usuario',read_only=True)
    class Meta:
        model = Inquilino
        fields = ['id','estado', 'usuario','usuario_detail']
    
    
    
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
            rol_defecto = Rol.objects.get(nombre="inquilino")
            usuario.roles.set([rol_defecto])
        else:
            usuario.roles.set(roles_data)

        # Crear propietario ligado a usuario
        inquilino = Inquilino.objects.create(usuario=usuario, **validated_data)

        return inquilino
        
class MascotaSerializer(serializers.ModelSerializer):
    inquilino = serializers.PrimaryKeyRelatedField(queryset=Inquilino.objects.all())
    class Meta:
        model = Mascota
        fields = ['id','nombre', 'especie', 'raza', 'inquilino']
        
class OcupanteSerializer(serializers.ModelSerializer):
    contrato = serializers.PrimaryKeyRelatedField(queryset=Contrato.objects.all())
    persona = serializers.SerializerMethodField()
    class Meta:
        model = Ocupante
        fields = ['id','persona', 'estado', 'contrato']
        
    def get_persona(self, obj):
        # 1. Buscamos la Persona usando el campo 'persona_ci' del Ocupante
        try:
            # Usamos get_object_or_404 de Django para manejar el caso donde no exista
            persona = Persona.objects.get(ci=obj.persona_ci) 
            
            # 2. Serializamos el objeto Persona encontrado
            return PersonaSerializer(persona).data
        except Persona.DoesNotExist:
            return None # Devolver None si la persona no se encuentra
    
    

class ContratoSerializer(serializers.ModelSerializer):
    vivienda = serializers.PrimaryKeyRelatedField(queryset=Vivienda.objects.all(),write_only=True)
    inquilino = serializers.PrimaryKeyRelatedField(queryset=Inquilino.objects.all(),write_only=True)
    inquilino_detail = InquilinoSerializer(source='inquilino',read_only=True)
    vivienda_detail = ViviendaSerializer(source='vivienda',read_only=True)
    
    ocupantes_ci = serializers.ListField(
        child=serializers.CharField(), write_only=True
    )

    class Meta:
        model = Contrato
        fields = ['id','descripcion','inquilino','inquilino_detail','vivienda_detail',
                  'fecha_ingreso', 'fecha_salida', 'porcentaje_expensa', 'tipo_renta',
                  'vivienda','vivienda_detail','ocupantes_ci','estado']
        
    def create(self, validated_data):
        ocupantes_ci = validated_data.pop("ocupantes_ci", [])
        contrato = super().create(validated_data)
        for ci in ocupantes_ci:
            try:
                Ocupante.objects.create(contrato=contrato, persona_ci=ci)
            except Persona.DoesNotExist:
                raise serializers.ValidationError(
                    {"ocupantes_ci": f"La persona con CI {ci} no existe"}
                )

        return contrato





class ContratoDetallesSerializer(serializers.Serializer):
   
    contrato = ContratoSerializer(read_only=True)
   
    ocupantes = OcupanteSerializer(many=True, read_only=True)
        
