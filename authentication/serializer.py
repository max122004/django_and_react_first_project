from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from authentication.models import User


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validates_data):
        user = super().create(validates_data)
        user.set_password(user.password)
        user.save()
        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        user = self.user
        profile_serializer = UserProfileSerializer(user)

        # Добавьте возвращаемые данные
        data.update({
            'id': user.id,
            'username': user.username,
            'image': profile_serializer.data.get('image'),
            'sex': profile_serializer.data.get('sex'),
            'first_name': profile_serializer.data.get('first_name'),
            'last_name': profile_serializer.data.get('last_name'),
            'is_active': user.is_active,
            'email': user.email,
        })

        return data


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'image', 'sex']


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['image', 'first_name', 'last_name', 'username', 'is_active', 'email']


class UserDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'image', 'sex', 'first_name', 'last_name', 'username', 'is_active', 'email']