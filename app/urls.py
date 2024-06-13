from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from app import settings

urlpatterns = [
    path("__debug__/", include("debug_toolbar.urls")),
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path("", include("api.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
