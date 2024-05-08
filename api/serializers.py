from rest_framework import serializers
from . import models


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Device
        fields = "__all__"


class ReadingRecordSerializer(serializers.ModelSerializer):
    device_id = serializers.IntegerField(required=True)
    sensors = serializers.JSONField(required=True)

    class Meta:
        model = models.ReadingRecord
        fields = ["device_id", "sensors"]

    def create(self, data):
        device_id = data.get("device_id")
        sensors = data.get("sensors")

        try:
            device = models.Device.objects.get(device_id=device_id)

            if not len(sensors):
                raise serializers.ValidationError(
                    {"error": f"No sensor value provided"}
                )

            for key, value in sensors.items():
                readingRecord = models.ReadingRecord.objects.create(
                    value=value, sensor_id=key, device_id=device.id
                )

            return readingRecord

        except models.Device.DoesNotExist:
            raise serializers.ValidationError(
                {"error": f"Device Id {device_id} does not exist"}
            )
