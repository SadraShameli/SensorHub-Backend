from rest_framework import serializers
from rest_framework.serializers import Serializer, ModelSerializer

from django.db import models
from . import models


class SensorSerializer(ModelSerializer):
    class Meta:
        model = models.Sensor
        fields = "__all__"


class LocationSerializer(ModelSerializer):
    class Meta:
        model = models.Location
        fields = "__all__"


class DeviceSerializer(ModelSerializer):
    class Meta:
        model = models.Device
        fields = "__all__"


class ReadingSerializer(ModelSerializer):
    class Meta:
        model = models.Reading
        fields = "__all__"


class ReadingCreateSerializer(Serializer):
    device_id = serializers.IntegerField(required=True)
    sensors = serializers.JSONField(required=True)

    class Meta:
        fields = "__all__"

    def validate_device_id(self, device_id):
        try:
            return models.Device.objects.get(device_id=device_id)
        except Exception as e:
            raise serializers.ValidationError(e)

    def validate_sensors(self, sensors):
        try:
            return [models.Sensor.objects.get(sensor_id=sensor) for sensor in sensors]
        except Exception as e:
            raise serializers.ValidationError(e)


class RecordingSerializer(ModelSerializer):
    class Meta:
        model = models.Recording
        fields = "__all__"


class RecordingCreateSerializer(Serializer):
    device_id = serializers.IntegerField(required=True)
    file = serializers.FileField(required=True)

    class Meta:
        fields = "__all__"

    def validate_device_id(self, device_id):
        try:
            return models.Device.objects.get(device_id=device_id)
        except Exception as e:
            raise serializers.ValidationError(e)