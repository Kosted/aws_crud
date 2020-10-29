
from model_mommy import mommy
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from core.models import User


class TestFactory(APITestCase):
    def setUp(self):
        self.user = mommy.make(User, is_superuser=True)
        self.password = "test"
        self.user.set_password(self.password)
        self.user.save()
        url = reverse("user_auth")
        token = self.client.post(url, {"username": self.user.username, "password": self.password}, format="json").json()
        self.auth_headers = {"HTTP_AUTHORIZATION": f"Token {token['token']}"}
