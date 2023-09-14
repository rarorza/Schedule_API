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
        ]

    def validate_date_time(self, value):
        """Validate if data_time is not in the past

        Keyword arguments:
        value -- body request data
        Return: datetime obj
        """

        if value < timezone.now():
            raise serializers.ValidationError(
                "Scheduling cannot be done in the past",
            )
        return value
