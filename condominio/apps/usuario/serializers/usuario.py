from rest_framework import serializers
from ..models import User, Persona

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'ci', 'telefono']

class UserSerializer(serializers.ModelSerializer):
    persona = PersonaSerializer()

    class Meta:
        model = User
        fields = ['username', 'email', 'persona']
