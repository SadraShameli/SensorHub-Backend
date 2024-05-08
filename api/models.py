from django.db import models


class Sensor(models.Model):
    class SensorTypes(models.TextChoices):
        TEMPERATURE = "Temperature"
        HUMIDITY = "Humidity"
        GASRESISTANCE = "GasResistance"
        AIRPRESSURE = "AirPressure"
        ALTITUDE = "Altitude"
        RPM = "RPM"
        SOUND = "Sound"

    created_at = models.DateTimeField(auto_now_add=True)
    sensor_id = models.IntegerField()
    type = models.CharField(choices=SensorTypes.choices, max_length=25, unique=True)
    unit = models.CharField(max_length=25)

    def __str__(self):
        return self.type


class Location(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    location_id = models.IntegerField()
    name = models.CharField(max_length=100)
    location_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Device(models.Model):
    class DeviceTypes(models.TextChoices):
        SOUND = "Sound"
        SENSOR = "Sensor"

    created_at = models.DateTimeField(auto_now_add=True)
    device_id = models.IntegerField()
    name = models.CharField(max_length=100)
    type = models.CharField(choices=DeviceTypes.choices, max_length=25)
    register_interval = models.IntegerField()
    loudness_threshold = models.IntegerField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ReadingRecord(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    value = models.IntegerField()
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

    def __str__(self):
        return self.created_at.__str__()
