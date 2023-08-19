import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.staff.factories import DepartmentFactory
from apps.users.factories import UserFactory


class TestEmployeeRegister(APITestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create(email="userexist@gmail.com")
        self.url = reverse("staff-register")
        self.department = DepartmentFactory.create()

        user_data = {
            "email": "email@gmail.com",
            "password": "123456",
            "password_confirm": "123456",
        }
        self.body = {"department": self.department.id, "user": user_data}

    def test_register_employee_correct(self):
        response = self.client.post(
            self.url, data=json.dumps(self.body), content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_register_employee_existing_email(self):
        self.body.get("user").update({"email": "userexist@gmail.com"})
        response = self.client.post(
            self.url, data=json.dumps(self.body), content_type="application/json"
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data.get("user").get("email")[0],
            "user with this email already exists.",
        )

    def test_register_employee_unmatched_password(self):
        self.body.get("user").update({"password_confirm": "anotherpassword"})
        response = self.client.post(
            self.url, data=json.dumps(self.body), content_type="application/json"
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data.get("user").get("password_confirm")[0],
            "Password and Password Confirm fields must have the same value.",
        )

    def test_register_employee_password_less_than_8(self):
        self.body.get("user").update({"password": "passw", "password_confirm": "passw"})
        response = self.client.post(
            self.url, data=json.dumps(self.body), content_type="application/json"
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data.get("user").get("password")[0],
            "Ensure this field has at least 8 characters.",
        )

    def test_register_employee_invalid_email(self):
        self.body.get("user").update({"email": "email1"})
        response = self.client.post(
            self.url, data=json.dumps(self.body), content_type="application/json"
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data.get("user").get("email")[0], "Enter a valid email address."
        )
