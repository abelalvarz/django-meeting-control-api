from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class TimeSlot(models.Model):
    slot = models.CharField(max_length=50)

    def __str__(self):
        return self.slot


class Meeting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timeSlot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)
