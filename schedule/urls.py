from django.urls import path

from schedule import views

app_name = "schedule"

urlpatterns = [
    path("schedules/", views.Schedules.as_view(), name="schedules"),
    path(
        "schedules/<int:id>/",
        views.SchedulingDetail.as_view(),
        name="scheduling",
    ),
    path("workers/", views.Workers.as_view(), name="workers"),
]
