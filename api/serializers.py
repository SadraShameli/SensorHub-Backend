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


class RecordingSerializer(ModelSerializer):
    class Meta:
        model = models.Recording
        fields = "__all__"


class ReadingCreateSerializer(Serializer):
    sensors = serializers.JSONField()
    device_id = serializers.IntegerField()
    location_id = serializers.IntegerField(required=False)

    class Meta:
        fields = "__all__"

    def validate_sensors(self, sensors):
        try:
            if len(sensors) == 0:
                raise serializers.ValidationError("No sensors provided")

            return [models.Sensor.objects.get(id=sensor) for sensor in sensors]
        except Exception as e:
            raise serializers.ValidationError(e)

    def validate_device_id(self, device_id):
        try:
            device = models.Device.objects.get(device_id=device_id)
            self.location_id = device.location.pk
            return device.pk
        except Exception as e:
            raise serializers.ValidationError(e)


class RecordingCreateSerializer(Serializer):
    file = serializers.FileField()
    device_id = serializers.IntegerField()
    location_id = serializers.IntegerField(required=False)

    class Meta:
        fields = "__all__"

    def validate_device_id(self, device_id):
        try:
            device = models.Device.objects.get(device_id=device_id)
            isOfType = list(device.sensors.filter(pk=7))

            if len(isOfType) == 0:
                raise serializers.ValidationError("Device type is not Recording")

            self.location_id = device.location.pk
            return device
        except Exception as e:
            raise serializers.ValidationError(e)

    def create(self, validated_data):
        return models.Recording.objects.create(
            file=validated_data["file"],
            device=validated_data["device_id"],
            location_id=self.location_id,
        )
