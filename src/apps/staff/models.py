from django.db import models

from apps.base.models import BaseModel


class Department(BaseModel):
    name = models.CharField(max_length=128, help_text="Department")


class Employee(BaseModel):
    user = models.OneToOneField(
        to="users.User",
        on_delete=models.CASCADE,
        related_name="employee",
        help_text="User",
    )
    department = models.ForeignKey(
        to=Department, on_delete=models.CASCADE, help_text="Department"
    )
