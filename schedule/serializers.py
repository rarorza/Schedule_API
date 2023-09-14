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
