from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("civicmap.urls")),
    path("infos/", include("civiclapp.urls")),
]
