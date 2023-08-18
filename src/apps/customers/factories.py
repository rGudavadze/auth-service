import factory
from factory.django import DjangoModelFactory

from apps.users.factories import UserFactory


class CustomerFactory(DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    identify = factory.Faker("ssn")
    name = factory.Faker("company")

    class Meta:
        model = "customers.Customer"
