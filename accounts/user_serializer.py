from django.db.models.fields import IntegerField
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password


from .models import  User


class UserSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    email = serializers.CharField()
    roles=serializers.CharField()
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    #password2 = serializers.CharField(write_only=True, required=True)
    
    def create(self, validated_data):
        user =User.objects.create(**validated_data)
        user.set_password(validated_data['password'])

        return user


