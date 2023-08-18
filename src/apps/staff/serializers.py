from rest_framework import serializers

from apps.staff.models import Department, Employee
from apps.users.serializers import UserSerializer


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = (
            "id",
            "name",
        )
        extra_kwargs = {"id": {"read_only": True}}


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            "id",
            "user",
            "department",
        )
        extra_kwargs = {"id": {"read_only": True}}


class EmployeeRegisterSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Employee
        fields = ("id", "department", "user")

    def create(self, validated_data):
        user_serializer = UserSerializer(data=validated_data.pop("user"))
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()

        validated_data.update({"user": user})
        employee = super().create(validated_data)

        return employee
