from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


class Room(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price_per_night = models.FloatField()
    address = models.CharField(max_length=255)
    guest_capacity = models.IntegerField()
    beds = models.IntegerField()
    internet = models.BooleanField()
    breakfast = models.BooleanField()
    air_conditioned = models.BooleanField()
    pets_allowed = models.BooleanField()
    room_cleaning = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class RoomImage(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="images")
    image = CloudinaryField("rooms")

    def __str__(self):
        return self.room.name


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="bookings")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="my_bookings")
    check_in_date = models.DateTimeField()
    check_out_date = models.DateTimeField()
    amount_paid = models.FloatField()
    day_of_stay = models.IntegerField()
    paid_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
