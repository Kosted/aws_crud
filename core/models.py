from django.contrib.auth import models as django_models
from django.urls import reverse


class User(django_models.AbstractUser):
    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
