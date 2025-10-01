# serializers.py
from rest_framework import serializers

class FacialSerializer(serializers.Serializer):
    image = serializers.ImageField(required=True)
