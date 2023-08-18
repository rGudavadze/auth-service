import factory
from factory.django import DjangoModelFactory


class UserFactory(DjangoModelFactory):
    email = factory.Faker("email")
    password = factory.Faker("password")

    class Meta:
        model = "users.User"
