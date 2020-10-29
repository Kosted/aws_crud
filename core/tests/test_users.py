from rest_framework import status
from rest_framework.reverse import reverse

from core.tests.utils import TestFactory


class UserTestCase(TestFactory):
    def setUp(self):
        super().setUp()

    def test_create_user_success(self):
        url = reverse("users-list")
        response = self.client.get(url, **self.auth_headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
