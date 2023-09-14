from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Scheduling
from .serializers import SchedulingSerializer


@api_view(http_method_names=["GET", "POST"])
def schedules_list(request):
    if request.method == "GET":
        objects = get_list_or_404(Scheduling, is_canceled=False)
        serializer = SchedulingSerializer(objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == "POST":
        body_request = request.data
        serializer = SchedulingSerializer(data=body_request)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(http_method_names=["GET", "PUT", "PATCH", "DELETE"])
# def scheduling(request):
#     ...
