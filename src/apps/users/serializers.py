from rest_framework import serializers

from apps.users.models import User
from utils.auth import TokenVerification
from utils.exceptions import (
    InvalidEmailOrPasswordException,
    InvalidTokenTypeException,
)
from utils.validators import PasswordMatchValidator


class UserSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(help_text="Password Confirm")

    class Meta:
        model = User
        fields = (
            "id",
            "email",
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

    def to_representation(self, instance: User):
        return {"detail": f"Hey {instance.email}, your account has been created."}


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


class RefreshTokenSerializer(serializers.Serializer):
    refresh_token = serializers.CharField(write_only=True)
    payload = serializers.DictField(read_only=True)

    def validate(self, attrs: dict):
        attrs = super().validate(attrs)

        token_payload = TokenVerification.decode_token(attrs.get("refresh_token"))
        if token_payload.get("token_type") != "refresh":
            raise InvalidTokenTypeException()

        attrs["payload"] = token_payload

        return attrs
