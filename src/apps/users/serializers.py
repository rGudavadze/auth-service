from rest_framework import serializers

from apps.users.models import User
from utils.validators import PasswordMatchValidator


class RegisterSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(help_text="Password Confirm")

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "username",
            "password",
            "password_confirm",
        )
        extra_kwargs = {
            "id": {"read_only": True},
            "password": {"write_only": True},
            "password_confirm": {"write_only": True},
        }
        validators = [PasswordMatchValidator()]

    def create(self, validated_data):
        validated_data.pop("password_confirm")
        instance = User.objects.create_user(**validated_data)
        return instance
