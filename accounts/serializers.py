from django.contrib.auth import get_user_model, password_validation
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from django.contrib.auth.models import BaseUserManager

User = get_user_model()

class EmptySerializer(serializers.Serializer):
    pass

class UserRegisterSerializer(serializers.ModelSerializer):
    """
    A user serializer for registering the user
    """

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'phone' , 'avatar',)

    def validate_email(self, value):
        user = User.objects.filter(email=email)
        if user:
            raise serializers.ValidationError("Email is already taken")
        return BaseUserManager.normalize_email(value)

    def validate_password(self, value):
        password_validation.validate_password(value)
        return value


class AuthAccountSerializer(serializers.ModelSerializer):
    auth_token = serializers.SerializerMethodField()

    class Meta:
         model = User
         fields = ('id', 'email', 'first_name', 'last_name', 'phone' , 'avatar' ,'is_active', 'is_staff')
         read_only_fields = ('id', 'is_active', 'is_staff')
    
    def get_auth_token(self, obj):
        token = Token.objects.create(user=obj)
        return token.key

class AccountLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=300, required=True)
    password = serializers.CharField(required=True, write_only=True)