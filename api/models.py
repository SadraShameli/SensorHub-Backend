from django.db import models


class Sensor(models.Model):
    class SensorTypes(models.TextChoices):
        TEMPERATURE = "Temperature"
        HUMIDITY = "Humidity"
        GASRESISTANCE = "GasResistance"
        AIRPRESSURE = "AirPressure"
        ALTITUDE = "Altitude"
        LOUDNESS = "Loudness"
        RPM = "RPM"

    created_at = models.DateTimeField(auto_now_add=True)
    type = models.CharField(choices=SensorTypes.choices,
                            max_length=25, unique=True)
    unit = models.CharField(max_length=25)
    sensor_id = models.IntegerField(unique=True)

    def __str__(self):
        return self.type


class Location(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    location_name = models.CharField(max_length=100, unique=True)
    location_id = models.IntegerField(unique=True)

    def __str__(self):
        return self.name


class Device(models.Model):
    class DeviceTypes(models.TextChoices):
        RECORDING_DEVICE = "Recording Device"
        READING_DEVICE = "Reading Device"

    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    type = models.CharField(choices=DeviceTypes.choices, max_length=25)
    device_id = models.IntegerField(unique=True)
    register_interval = models.IntegerField()
    loudness_threshold = models.IntegerField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Reading(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    value = models.FloatField()
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

    def __str__(self):
        return self.created_at.__str__()


class Recording(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    file = models.FileField(upload_to='recordings/')

    def __str__(self):
        return self.file.name
