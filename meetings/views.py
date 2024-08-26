from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from meetings.serivces.UserService import UserService

from .models import Meeting, TimeSlot, User
from .serializers import MeetingSerializer, TimeSlotSerializer, UserSerializer
from .utils import create_response

# Create your views here.


class UsersView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class TimeSlotList(viewsets.ModelViewSet):
    serializer_class = TimeSlotSerializer
    queryset = TimeSlot.objects.all()


class MeetingList(viewsets.ModelViewSet):
    serializer_class = MeetingSerializer
    queryset = Meeting.objects.all()


class BusyTimeSlotWithUser(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = []
        for slot in serializer.data:
            time_slot = TimeSlot.objects.get(id=slot["id"])
            users = UserService.get_users_on_meeting(time_slot)
            if users:
                slot["users"] = users
                data.append(slot)

        return create_response(data)


class AvailableTimeSlotWithUser(viewsets.ModelViewSet):
    serializer_class = TimeSlotSerializer
    queryset = TimeSlot.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = []
        for slot in serializer.data:
            time_slot = TimeSlot.objects.get(id=slot["id"])
            users = UserService.get_users_available(time_slot)
            if len(users) >= 3:
                slot["users"] = users
                data.append(slot)

        return create_response(data)
