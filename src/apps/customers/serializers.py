from rest_framework import serializers

from apps.customers.models import Customer
from apps.users.serializers import UserSerializer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = (
            "id",
            "user",
            "identity_number",
            "name",
        )
        extra_kwargs = {"id": {"read_only": True}}


class CustomerRegisterSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Customer
        fields = ["id", "identity_number", "name", "user"]

    def create(self, validated_data):
        user_serializer = UserSerializer(data=validated_data.pop("user"))
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()

        validated_data.update({"user": user})
        customer = super().create(validated_data)

        return customer
