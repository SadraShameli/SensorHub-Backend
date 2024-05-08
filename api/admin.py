from django.contrib import admin
from .models import Sensor, ReadingRecord, Device, Location

admin.site.register(
    [
        Sensor,
        ReadingRecord,
        Device,
        Location,
    ]
)
