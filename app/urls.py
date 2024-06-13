from django.contrib import admin
from django.views.static import serve
from django.conf.urls.static import static
from django.urls import path, include, re_path
from app import settings

urlpatterns = [
    path("__debug__/", include("debug_toolbar.urls")),
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path("", include("api.urls")),
]

urlpatterns += [
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT})
]
