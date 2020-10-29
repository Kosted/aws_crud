from django.contrib.auth.models import Group
from rest_framework import serializers

from core.models import User


class UserSerializer(serializers.ModelSerializer):
    groups = serializers.SlugRelatedField(queryset=Group.objects.all(), slug_field="name", many=True)
    password = serializers.CharField(required=False, write_only=True, max_length=128)

    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "password", "groups", "is_active", "last_login",
                  "is_superuser"]
        read_only_fields = ("id", "is_superuser")
