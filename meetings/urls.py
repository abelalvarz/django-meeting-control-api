from django.urls import include, path
from rest_framework import routers

from .views import (
    AvailableTimeSlotWithUser,
    BusyTimeSlotWithUser,
    TimeSlotList,
    UsersView,
)

router = routers.DefaultRouter()
router.register(r"users", UsersView, "users")
router.register(r"times", TimeSlotList, "times")
router.register(r"available-time", AvailableTimeSlotWithUser, "available-time")
router.register(r"busy-time", BusyTimeSlotWithUser, "busy-time")

urlpatterns = [
    path("v1/", include(router.urls)),
]
