from rest_framework import serializers
from accounts.models import User
from django.contrib import auth
from rest_framework import exceptions

class RegisterSerializer(serializers.ModelSerializer):
    '''
    Registration Serializer
    '''

    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'password', 'name', 'is_organization')
        extra_kwargs = {'password': {'write_only': True}}
    
    def validate(self, attrs):
        '''
        validate method - validates the instance passed to the serializer
        '''

        username = attrs.get('username', '')

        if not username.isalnum():
            raise serializers.ValidationError("Username should be alphnumeric")
        
        return attrs
    

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.ModelSerializer):
    '''
    Login serializer
    '''
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(max_length=255)
    username = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(min_length=1, write_only=True)
    tokens = serializers.SerializerMethodField()
    
    
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'tokens')

    
    def validate(self, attrs):
        '''
        validate method - validates the instance passed to the serializer
        '''

        email = attrs.get('email', '')
        password = attrs.get('password', '')

        user = auth.authenticate(email=email, password=password)

        if not user:
            raise exceptions.AuthenticationFailed('Invalid credentials, try again')

        if not user.is_active:
            raise exceptions.AuthenticationFailed('Account Disabled, contact admin')

        return {
            "id":user.id,
            "email": user.email,
            "username": user.username,
            "tokens": user.tokens
        }


        

