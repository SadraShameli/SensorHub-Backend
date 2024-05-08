from rest_framework.response import Response
from rest_framework.decorators import api_view


from . import models
from . import serializers


@api_view(["GET"])
def getRoutes(request):
    routes = [
        "GET /getDeviceProperties/:id",
        "POST /registerReadingRecord/",
    ]
    return Response(routes)


@api_view(["GET"])
def getDeviceProperties(request, device_id):
    try:
        device = models.Device.objects.get(device_id=device_id)
        serializer = serializers.DeviceSerializer(device, many=False)
        return Response(serializer.data)

    except models.Device.DoesNotExist:
        return Response({"error": f"Device Id {device_id} does not exist"}, status=404)


@api_view(["POST"])
def registerReadingRecord(request):
    readingRecord = serializers.ReadingRecordSerializer(data=request.data)

    if readingRecord.is_valid(raise_exception=True):
        readingRecord.save()
        return Response(status=200)
