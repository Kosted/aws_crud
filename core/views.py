import logging

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from core.models import User
from core.serializers import UserSerializer

logger = logging.getLogger(__name__)


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def finalize_response(self, request, response, *args, **kwargs):
        logger.info(f"User {request.user.id} performed {self.action} on {request.path} URL")
        return super().finalize_response(request, response, *args, **kwargs)
