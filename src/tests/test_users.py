from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.users.models import User


class TestUserLogin(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(email="email@gmail.com", password="password")
        self.url = reverse("user-login")
        self.body = dict(email="email@gmail.com", password="password")

    def test_login_correct(self):
        response = self.client.post(self.url, data=self.body)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "access")

    def test_login_incorrect_email(self):
        self.body.update({"email": "incorrect@gmail.com"})
        response = self.client.post(self.url, data=self.body)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(
            response.data.get("detail"),
            "No active account found with the given credentials",
        )

    def test_login_incorrect_password(self):
        self.body.update({"password": "password123"})
        response = self.client.post(self.url, data=self.body)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(
            response.data.get("detail"),
            "No active account found with the given credentials",
        )
