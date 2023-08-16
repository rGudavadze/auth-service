from django.db import models

from apps.base.models import BaseModel


class Customer(BaseModel):
    user = models.OneToOneField(
        to="users.User",
        on_delete=models.CASCADE,
        related_name="customer",
        help_text="User",
    )
    identity_number = models.CharField(max_length=128, help_text="Identity Number")
    name = models.CharField(max_length=128, help_text="Name")

    def __str__(self):
        return f"{self.name} - {self.identity_number}"
