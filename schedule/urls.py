from django.urls import path

from schedule import views

app_name = "schedule"

urlpatterns = [
    path("schedules/", views.schedules_list, name="schedules"),
    # path("schedules/<int:id>/", views.scheduling, name="scheduling"),
]
