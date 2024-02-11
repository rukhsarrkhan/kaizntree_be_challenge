from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed

class UserRegistrationSerializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=68, min_length=6, write_only=True)
    password2=serializers.CharField(max_length=68, min_length=6, write_only=True)

    class Meta:
        model=User
        fields=['email','password','password2']

    def validate(self, attrs):
        password=attrs.get('password','')
        password2=attrs.get('password2','')
        if password != password2:
            raise serializers.ValidationError("Passwords do not match")

        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(
            email = validated_data['email'],
            password = validated_data.get('password')
        )
        return user
    
class UserLoginSerializer(serializers.ModelSerializer):
    email=serializers.CharField(max_length=255, min_length=6)
    password=serializers.CharField(max_length=68, write_only=True)
    access_token=serializers.CharField(max_length=255, read_only=True)
    refresh_token=serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model=User
        fields=['email','password','access_token','refresh_token']
    
    def validate(self, attrs):
        email=attrs.get('email','')
        password=attrs.get('password','')
        request = self.context.get('request')
        user=authenticate(request, email=email, password=password)
        if not user:
            raise AuthenticationFailed("Invalid credentials, Try again")
        # if not user.is_verified:
        #     raise AuthenticationFailed("Email is not verified")
        user_tokens = user.tokens()
        
        return {
            'email': user.email,
            'access_token': str(user_tokens.get('access')),
            'refresh_token': str(user_tokens.get('refresh'))
        }