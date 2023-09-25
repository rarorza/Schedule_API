from django.contrib.auth.models import User
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Scheduling
from .serializers import SchedulingSerializer, WorkerSerializer


class Schedules(APIView):
    def get(self, request):
        objects = get_list_or_404(Scheduling, is_canceled=False)
        serializer = SchedulingSerializer(objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        body_request = request.data
        serializer = SchedulingSerializer(data=body_request)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SchedulingDetail(APIView):
    def get(self, request, id):
        object = get_object_or_404(Scheduling, id=id)
        serializer = SchedulingSerializer(object)
        return Response(serializer.data)

    def patch(self, request, id):
        object = get_object_or_404(Scheduling, id=id)
        body_request = request.data
        serializer = SchedulingSerializer(
            object, data=body_request, partial=True
        )  # noqa 501
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        object = get_object_or_404(Scheduling, id=id)
        body_request = request.data
        serializer = SchedulingSerializer(object, data=body_request)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        object = get_object_or_404(Scheduling, id=id)
        object.is_canceled = True
        object.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Workers(APIView):
    def get(self, request):
        workers = User.objects.all()
        serializer = WorkerSerializer(workers, many=True)
        return Response(serializer.data)
