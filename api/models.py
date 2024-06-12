from django.db import models


class Location(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    location_name = models.CharField(max_length=100, unique=True)
    location_id = models.IntegerField(unique=True)

    def __str__(self):
        return self.name


class Sensor(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, unique=True)
    unit = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Device(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    device_id = models.IntegerField(unique=True)
    register_interval = models.IntegerField()
    loudness_threshold = models.IntegerField()
    sensors = models.ManyToManyField(Sensor)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Reading(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    value = models.FloatField()
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

    def __str__(self):
        return self.created_at.__str__()


class Recording(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to="recordings/")
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

    def __str__(self):
        return self.file.name
