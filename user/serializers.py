from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'ism', 'familiya', 'date_joined')


class UserPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')

        extra_kwargs = {
            'password': {
                'write_only': True,
            },
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserUpdateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=False)
    ism = serializers.CharField(required=False, max_length=255)
    familiya = serializers.CharField(required=False, max_length=255)

    class Meta:
        model = User
        fields = ('id', 'email', 'ism', 'familiya')


class ChangePasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'password')

        extra_kwargs = {
            'password': {'write_only': True},
        }


class ChangeUsernameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')
