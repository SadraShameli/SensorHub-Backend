from django.contrib import admin
from .models import Sensor, Location, Device, Reading, Recording

admin.site.register(
    [
        Sensor,
        Location,
        Device,
        Reading,
        Recording,
    ]
)
