from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models

from apps.base.models import BaseModel
from apps.users.managers import CustomUserManager


class User(AbstractUser, BaseModel):
    email = models.EmailField(
        max_length=128,
        unique=True,
        help_text="Email",
    )
    password = models.CharField(
        max_length=512,
        help_text="Password",
        validators=[
            MinLengthValidator(8),
        ],
    )
    username = models.CharField(max_length=128, null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
