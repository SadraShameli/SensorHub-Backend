
from datetime import datetime
from django.shortcuts import get_object_or_404, render
from django.core.files.base import ContentFile
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from api.utils import applyEffects
from . import models, serializers


def index(request):
    return render(request, 'index.html')


class SensorViewSet(viewsets.ModelViewSet):
    queryset = models.Sensor.objects.all()
    serializer_class = serializers.SensorSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = models.Location.objects.all()
    serializer_class = serializers.LocationSerializer

    def retrieve(self, request, pk):
        queryset = models.Location.objects.all()
        location = get_object_or_404(queryset, location_id=pk)
        serializer = self.get_serializer(location)
        return Response(serializer.data)


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = models.Device.objects.all()
    serializer_class = serializers.DeviceSerializer

    def retrieve(self, request, pk):
        queryset = models.Device.objects.all()
        device = get_object_or_404(queryset, device_id=pk)
        serializer = self.get_serializer(device)
        return Response(serializer.data)


class ReadingViewSet(viewsets.ModelViewSet):
    queryset = models.Reading.objects.all()
    serializer_class = serializers.ReadingSerializer

    def create(self, request):
        try:
            readingCreateSerializer = serializers.ReadingCreateSerializer(
            data=request.data)
            readingCreateSerializer.is_valid(raise_exception=True)
            data = readingCreateSerializer.validated_data

            for sensor in data["sensors"]:
                reading = models.Reading.objects.create(
                value=request.data["sensors"][f"{sensor.id}"], sensor=sensor, device_id=data["device_id"], location_id=readingCreateSerializer.location_id)
                reading.save()

        except Exception as e:
                return Response(data={"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(status=status.HTTP_201_CREATED)


class RecordingViewSet(viewsets.ModelViewSet):
    queryset = models.Recording.objects.all()
    serializer_class = serializers.RecordingSerializer

    def create(self, request, pk):
        try:
            recording = applyEffects(request.stream.body)
            recordingCreateSerializer = serializers.RecordingCreateSerializer(
              data={"file": ContentFile(recording, name=f"{datetime.now().strftime("%B %d, %Y - %H.%M")}.wav"), "device_id": pk})
            recordingCreateSerializer.is_valid(raise_exception=True)
            recordingCreateSerializer.save()

        except Exception as e:
            return Response(data={"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(status=status.HTTP_201_CREATED)
