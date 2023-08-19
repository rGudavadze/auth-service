import factory
from factory.django import DjangoModelFactory

from apps.users.factories import UserFactory


class DepartmentFactory(DjangoModelFactory):
    name = factory.Faker("name")

    class Meta:
        model = "staff.Department"


class EmployeeFactory(DjangoModelFactory):
    department = factory.SubFactory(DepartmentFactory)
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = "staff.Employee"
