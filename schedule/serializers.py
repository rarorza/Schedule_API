from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework import serializers

from schedule.models import Scheduling


class SchedulingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scheduling
        fields = [
            "id",
            "date_time",
            "customer_name",
            "email",
            "phone",
            "worker",
            "is_canceled",
        ]

    worker = serializers.CharField()

    def validate_date_time(self, value) -> object:
        """Validate if data_time is not in the past

        Keyword arguments:
        value -- date request data
        Return: datetime obj
        """

        if value < timezone.now():
            raise serializers.ValidationError(
                "Scheduling cannot be done in the past",
            )
        return value

    def validate_worker(self, value) -> User:
        """Validate if worker username exist to create a scheduling

        Keyword arguments:
        value -- worker username request data
        Return: User instance
        """
        try:
            worker_obj = User.objects.get(username=value)
        except User.DoesNotExist:
            raise serializers.ValidationError("username does not exist!")
        return worker_obj


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "schedules"]

    schedules = SchedulingSerializer(many=True, read_only=True)
