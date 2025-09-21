from rest_framework import serializers
from ..models import User
from django.contrib.auth import authenticate


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    
    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        
        if username and password:
            user = authenticate(username=username, password=password)
            user = User.objects.get(username=username)
            if  user is None:
                raise serializers.ValidationError('Usuario no encontrado')

        else:
            raise serializers.ValidationError('Debe proporcionar un nombre de usuario y una contraseña')
        
        attrs['user'] = user
        return attrs


    