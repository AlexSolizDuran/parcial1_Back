from rest_framework import serializers
from ..models import User, Persona,Rol
from ..utils import generar_vector_facial_opencv



class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ['id','nombre', 'apellido', 'ci', 'telefono','fecha_nacimiento','foto','genero','direccion']

    def create(self, validated_data):
        persona = super().create(validated_data)
        generar_vector_facial_opencv(persona)  # Generamos vector si hay foto
        return persona

    def update(self, instance, validated_data):
        persona = super().update(instance, validated_data)
        generar_vector_facial_opencv(persona)  # Re-generamos vector si actualizan foto
        return persona

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'email']

class UserSerializer(serializers.ModelSerializer):
    persona = PersonaSerializer()
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    roles = serializers.SlugRelatedField(
        many=True,
        queryset=Rol.objects.all(),
        slug_field='nombre',
        required=False,
        default=[],
    )


    class Meta:
        model = User
        fields = ['id','username','password', 'email', 'persona','roles','activo']
    
    def create(self, validated_data):
        persona_data = validated_data.pop('persona')
        roles_data = validated_data.pop('roles', [])
        password = validated_data.pop('password')

        persona = Persona.objects.create(**persona_data)
        user = User(persona=persona, **validated_data)
        user.set_password(password)
        user.save()

        # asignar roles
        user.roles.set(roles_data)

        return user

    def update(self, instance, validated_data):
        persona_data = validated_data.pop('persona', None)
        if persona_data:
            persona = instance.persona
            for attr, value in persona_data.items():
                setattr(persona, attr, value)
            persona.save()
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
            
