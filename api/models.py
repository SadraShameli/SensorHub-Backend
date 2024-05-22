from django.db import models


class Sensor(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, unique=True)
    unit = models.CharField(max_length=25)
    enabled = models.BooleanField()

    def __str__(self):
        return self.name


class Location(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    location_name = models.CharField(max_length=100, unique=True)
    location_id = models.IntegerField(unique=True)

    def __str__(self):
        return self.name


class Device(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    device_id = models.IntegerField(unique=True)
    register_interval = models.IntegerField()
    loudness_threshold = models.IntegerField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    sensor = models.ManyToManyField(Sensor)

    def __str__(self):
        return self.name


class Reading(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    value = models.FloatField()
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

    def __str__(self):
        return self.created_at.__str__()


class Recording(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    file = models.FileField(upload_to='recordings/')
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

    def __str__(self):
        return self.file.name
