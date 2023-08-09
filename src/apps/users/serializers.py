from rest_framework import serializers

from apps.users.models import User
from utils.exceptions import InvalidEmailOrPasswordException
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


class LoginSerializer(serializers.Serializer):
    user_id = serializers.UUIDField(read_only=True)
    email = serializers.EmailField(max_length=128, help_text="Email", write_only=True)

    password = serializers.CharField(
        max_length=128, help_text="Password", write_only=True
    )

    def validate(self, attrs: dict):
        attrs = super().validate(attrs)

        user = User.objects.filter(email=attrs.get("email")).first()
        if not (user and user.check_password(attrs.get("password"))):
            raise InvalidEmailOrPasswordException()

        attrs["user_id"] = user.id

        return attrs
