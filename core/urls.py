from django.urls import path, include, re_path
from django.views.generic import RedirectView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.reverse import reverse_lazy
from rest_framework.routers import DefaultRouter

from core.views import UserViewSet


router = DefaultRouter()
router.register(r"users", UserViewSet, "users")

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("api-token-auth/", obtain_auth_token, name="user_auth"),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),

    # the "api-root" from django rest-frameworks default router
    # http://www.django-rest-framework.org/api-guide/routers/#defaultrouter
    re_path(r"^$", RedirectView.as_view(url=reverse_lazy("api-root"), permanent=False)),
]
