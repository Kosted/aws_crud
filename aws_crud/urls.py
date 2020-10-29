from django.contrib import admin
from django.urls import path, include

from core.urls import urlpatterns as core_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(core_urls)),
]
