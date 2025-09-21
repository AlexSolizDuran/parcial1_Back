from rest_framework import serializers
from ..models import User, Persona

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'ci', 'telefono']

class UserSerializer(serializers.ModelSerializer):
    persona = PersonaSerializer()
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['username','password', 'email', 'persona']
    
    def create(self, validated_data):
        persona = validated_data.pop('persona') #estraemos los datos de persona
        password = validated_data.pop('password') 
        persona = Persona.objects.create(**persona) # creamos a personar
        user = User(persona=persona,**validated_data) # creamos a usuario
        user.set_password(password) #hasheamos contraseña
        user.save()
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
            
