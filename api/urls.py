from django.urls import path
from . import views

urlpatterns = [
    path("", views.getRoutes),
    path("getDeviceProperties/<int:device_id>/", views.getDeviceProperties),
    path("registerReadingRecord/", views.registerReadingRecord),
]
