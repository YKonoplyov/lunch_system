from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/user/", include("users.urls", namespace="users")),
    path(
        "api/lunch_service/",
        include("lunch_service.urls", namespace="lunch-service")
    ),
    path("__debug__/", include("debug_toolbar.urls")),
]
