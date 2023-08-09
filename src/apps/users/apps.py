import os

from django.apps import AppConfig
from django.contrib.auth import get_user_model


class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.users"

    @classmethod
    def ready(cls):
        try:
            user_model = get_user_model()
            if user_model.objects.filter(is_superuser=True).exists():
                return

            user_model.objects.create_superuser(
                email=os.environ.get("DJANGO_SUPERUSER_EMAIL"),
                password=os.environ.get("DJANGO_SUPERUSER_PASSWORD"),
            )

        except Exception as err:
            print(
                f"Found an error trying to create the superuser - {err}\n"
                "if you aren't running the user model migration yet, ignore this message."
            )
