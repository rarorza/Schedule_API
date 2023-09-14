from django.urls import path

from schedule import views

urlpatterns = [
    path("schedules/", views.index),
]
