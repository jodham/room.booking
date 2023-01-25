from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.
class Room(models.Model):
    room_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    capacity = models.IntegerField()
    description = models.TextField()
    # Images = models.ImageField(null=True, upload_to='room_images')

    def __str__(self):
        return self.room_name


class Boooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    no_of_users = models.IntegerField()
    time_booked = models.DateTimeField(default=timezone.now)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.BooleanField(default=True)


class Institution_details(models.Model):
    institution_name = models.CharField(max_length=150)
    institution_email = models.EmailField()
    motto = models.CharField(max_length=250)
    address = models.CharField(max_length=50)
    vision = models.TextField()
    mission = models.TextField()
