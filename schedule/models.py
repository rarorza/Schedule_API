from django.db import models


# Create your models here.
class Scheduling(models.Model):
    worker = models.ForeignKey(
        "auth.User", related_name="schedules", on_delete=models.CASCADE
    )
    date_time = models.DateTimeField()
    customer_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    is_canceled = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.customer_name} - {self.date_time}"
