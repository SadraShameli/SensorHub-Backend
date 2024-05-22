from rest_framework.routers import DefaultRouter
from django.urls import path

from . import views

router = DefaultRouter()
router.register('sensor', views.SensorViewSet)
router.register('location', views.LocationViewSet)
router.register('device', views.DeviceViewSet)
router.register('reading', views.ReadingViewSet)
router.register('recording', views.RecordingViewSet)

urlpatterns = [
    path('', views.index),
    path('recording/<int:pk>/',
         views.RecordingViewSet.as_view({"get": "retrieve", "post": "create"}))
] + router.urls
